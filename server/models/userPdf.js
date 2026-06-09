// server/models/userPdf.js
const db = require('./db');
const path = require('path');

/**
 * Save or update PDF path for a user.
 * @param {string} userId - User identifier.
 * @param {string} filePath - Absolute path where the PDF is stored.
 * @param {string} filename - Original filename (for display).
 */
async function savePdf(userId, filePath, filename) {
  const query = `INSERT INTO user_pdfs (user_id, pdf_path, filename, uploaded_at)
                 VALUES ($1, $2, $3, NOW())
                 ON CONFLICT (user_id) DO UPDATE SET
                   pdf_path = EXCLUDED.pdf_path,
                   filename = EXCLUDED.filename,
                   uploaded_at = NOW();`;
  await db.query(query, [userId, filePath, filename]);
}

/**
 * Retrieve the stored PDF path for a user.
 * @param {string} userId
 * @returns {string|null} Absolute path to PDF or null if none.
 */
async function getPdfPath(userId) {
  const result = await db.query(
    'SELECT pdf_path FROM user_pdfs WHERE user_id = $1',
    [userId]
  );
  if (result.rowCount === 0) return null;
  return result.rows[0].pdf_path;
}

module.exports = { savePdf, getPdfPath };
