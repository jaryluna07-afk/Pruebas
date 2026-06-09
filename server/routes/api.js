// server/routes/api.js
const express = require('express');
const router = express.Router();
const multer = require('multer');
const path = require('path');
const { saveSignature, getSignature } = require('../models/userSignature');
const { savePdf, getPdfPath } = require('../models/userPdf');

// Multer config – store PDFs in uploads folder per user
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    const userId = req.body.userId;
    const uploadPath = path.join(__dirname, '..', '..', 'uploads', userId);
    cb(null, uploadPath);
  },
  filename: (req, file, cb) => {
    cb(null, Date.now() + '-' + file.originalname);
  }
});
const upload = multer({
  storage,
  fileFilter: (req, file, cb) => {
    if (file.mimetype !== 'application/pdf') {
      return cb(new Error('Only PDF files are allowed'), false);
    }
    cb(null, true);
  },
  limits: { fileSize: 5 * 1024 * 1024 } // 5 MB limit
});

// Save HTML signature
router.post('/signature', async (req, res) => {
  const { userId, html } = req.body;
  if (!userId || !html) return res.status(400).json({ error: 'Missing parameters' });
  try {
    await saveSignature(userId, html);
    res.json({ success: true });
  } catch (e) {
    console.error(e);
    res.status(500).json({ error: 'Failed to save signature' });
  }
});

// Retrieve signature
router.get('/signature/:userId', async (req, res) => {
  const { userId } = req.params;
  try {
    const html = await getSignature(userId);
    res.json({ html });
  } catch (e) {
    console.error(e);
    res.status(500).json({ error: 'Failed to retrieve signature' });
  }
});

// Upload PDF (digital signature / certificate)
router.post('/upload-pdf', upload.single('pdf'), async (req, res) => {
  const { userId } = req.body;
  if (!userId) return res.status(400).json({ error: 'Missing userId' });
  try {
    const filePath = req.file.path;
    const filename = req.file.originalname;
    await savePdf(userId, filePath, filename);
    res.json({ success: true, filePath });
  } catch (e) {
    console.error(e);
    res.status(500).json({ error: 'PDF upload failed' });
  }
});

module.exports = router;
