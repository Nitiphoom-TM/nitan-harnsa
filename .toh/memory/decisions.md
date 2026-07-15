# Decisions

| Date | Decision | Reason |
|------|----------|--------|
| 2026-07-14 | ใช้ static HTML ไฟล์เดียว แทน Next.js | ไม่ต้องติดตั้งอะไร เปิดได้ทันที เหมาะกับให้เด็กใช้ ลดจุดพัง |
| 2026-07-14 | เสียง AI ใช้ Web Speech API (th-TH) | ฟรี ทำงานออฟไลน์ ไม่ต้องใช้ API key; macOS มีเสียง "Kanya" |
| 2026-07-14 | รูปประกอบเป็น SVG วาดในโค้ด | ไม่ต้องเรียก image-gen API, โหลดเร็ว, คมทุกขนาดจอ |
| 2026-07-14 | gradient id ใน SVG ต้อง unique ต่อรูป | id ซ้ำข้าม inline SVG ทำให้ท้องฟ้าเป็นสีขาว (แก้แล้วด้วย counter) |
| 2026-07-14 | ไฮไลต์คำใช้ fallback ตามเวลา ไม่พึ่ง onboundary อย่างเดียว | เสียงไทย "Kanya" บน macOS ไม่ยิง event onboundary เลย ต้องประมาณเวลา ~90ms/char |
| 2026-07-14 | speak() ต้องใช้ speakSession id กัน event เก่ามาล้างสถานะใหม่ | synth.cancel() ทำให้ onend/onerror ของเสียงเก่ายิงแบบ async แล้ว clearFallback ล้าง timer ของเสียงใหม่ |
| 2026-07-15 | ใช้ Edge Neural TTS แบบ pre-generate MP3 ไม่ใช่เรียกสดจากเบราว์เซอร์ | ทดสอบแล้ว endpoint ของ Bing ปฏิเสธ WebSocket จากเบราว์เซอร์ (opened:false) เพราะเบราว์เซอร์ส่ง Origin header ที่ลบไม่ได้ — edge-tts เรียกได้จาก Node/Python เท่านั้น |
| 2026-07-15 | ปรับความเร็วด้วย audio.playbackRate + preservesPitch | เปลี่ยนสดได้ขณะเล่นโดยเสียงไม่เพี้ยน และใช้ไฟล์ MP3 เดิมได้ ไม่ต้องสร้างเสียงหลายความเร็ว |
| 2026-07-15 | ไฮไลต์อ่านตามอิง audio.currentTime/duration | Edge TTS ไม่ส่ง WordBoundary สำหรับภาษาไทย (มีแต่ SentenceBoundary) แต่รู้ความยาวไฟล์จริง เลยกระจายตามสัดส่วนตัวอักษรได้แม่นกว่าเดิม |
| 2026-07-15 | เก็บ tools/gen_audio.py ไว้ใน repo | ถ้าแก้ข้อความนิทานต้องสร้างไฟล์เสียงใหม่ สคริปต์อ่านข้อความจาก index.html โดยตรงจึงไม่หลุด sync |
