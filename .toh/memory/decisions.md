# Decisions

| Date | Decision | Reason |
|------|----------|--------|
| 2026-07-14 | ใช้ static HTML ไฟล์เดียว แทน Next.js | ไม่ต้องติดตั้งอะไร เปิดได้ทันที เหมาะกับให้เด็กใช้ ลดจุดพัง |
| 2026-07-14 | เสียง AI ใช้ Web Speech API (th-TH) | ฟรี ทำงานออฟไลน์ ไม่ต้องใช้ API key; macOS มีเสียง "Kanya" |
| 2026-07-14 | รูปประกอบเป็น SVG วาดในโค้ด | ไม่ต้องเรียก image-gen API, โหลดเร็ว, คมทุกขนาดจอ |
| 2026-07-14 | gradient id ใน SVG ต้อง unique ต่อรูป | id ซ้ำข้าม inline SVG ทำให้ท้องฟ้าเป็นสีขาว (แก้แล้วด้วย counter) |
| 2026-07-14 | ไฮไลต์คำใช้ fallback ตามเวลา ไม่พึ่ง onboundary อย่างเดียว | เสียงไทย "Kanya" บน macOS ไม่ยิง event onboundary เลย ต้องประมาณเวลา ~90ms/char |
| 2026-07-14 | speak() ต้องใช้ speakSession id กัน event เก่ามาล้างสถานะใหม่ | synth.cancel() ทำให้ onend/onerror ของเสียงเก่ายิงแบบ async แล้ว clearFallback ล้าง timer ของเสียงใหม่ |
