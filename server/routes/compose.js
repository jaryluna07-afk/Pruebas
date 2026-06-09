// server/routes/compose.js
const express = require('express');
const router = express.Router();
const { getSignature } = require('../models/userSignature');
const { getPdfPath } = require('../models/userPdf');
const { sendMail } = require('../email/mailer');

/**
 * Expected payload:
 * {
 *   userId: string,
 *   to: string,
 *   subject: string,
 *   body: string   // plain text or HTML body supplied by client
 * }
 */
router.post('/send-email', async (req, res) => {
  const { userId, to, subject, body } = req.body;
  if (!userId || !to || !subject || !body) {
    return res.status(400).json({ error: 'Missing required fields' });
  }
  try {
    const signatureHtml = await getSignature(userId);
    const pdfPath = await getPdfPath(userId);
    const fullBody = `${body}<br/><br/>${signatureHtml}`;
    await sendMail({ to, subject, html: fullBody, attachmentPath: pdfPath });
    res.json({ success: true });
  } catch (e) {
    console.error(e);
    res.status(500).json({ error: 'Failed to send email' });
  }
});

module.exports = router;
