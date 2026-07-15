# Active

## Current Focus
เว็บนิทานเล่าเสียงสำหรับเด็ก "นิทานหรรษา" (index.html ไฟล์เดียว)

## In Progress
- [x] หน้าเลือกนิทาน 9 เรื่อง (กระต่ายกับเต่า, ลูกเป็ดขี้เหร่, ราชสีห์กับหนูน้อย, ลูกหมูสามตัว, เด็กเลี้ยงแกะ, มดกับตั๊กแตน, หมาจิ้งจอกกับองุ่น, กากับเหยือกน้ำ, สุนัขกับเงาในน้ำ)
- [x] ภาพประกอบ SVG ทุกฉาก + ตัวละคร (PIG, WOLF, HOUSE, BOY, SHEEP, ANT, HOPPER, FOX, CROW, PITCHER, GRAPES, DOG, BONE, ARBOR, STREAM, BRIDGE)
- [x] เสียง AI เล่าไทยจาก Edge Neural TTS (th-TH-PremwadeeNeural) เป็นไฟล์ MP3 41 ไฟล์ใน audio/
- [x] ปุ่มปรับความเร็ว 3 ระดับ (playbackRate + preservesPitch) + หยุด/เล่นต่อ
- [x] deploy ขึ้น GitHub Pages: https://nitiphoom-tm.github.io/nitan-harnsa/
- [x] แตะรูป/ปุ่มเพื่อฟัง, ก่อนหน้า/ถัดไป, จุดบอกฉาก, โหมดเล่าต่อเองทุกฉาก
- [x] คอนเฟตตีฉลองตอนจบเรื่อง
- [x] ไฮไลต์คำตามเสียงอ่าน (read-along/karaoke) — ใช้ onboundary ถ้ามี, ไม่มีก็ fallback ตามเวลา
- [x] ทดสอบผ่าน browser แล้ว (เสียง Kanya ทำงาน, ไฮไลต์เดินตามเสียง)

## Next Steps
- เพิ่มนิทานเรื่องใหม่ (เพิ่ม object ใน STORIES ได้เลย)
- เพิ่มเอฟเฟกต์เสียงประกอบ / เพลงพื้นหลัง
- deploy ขึ้นเว็บจริงถ้าต้องการแชร์
