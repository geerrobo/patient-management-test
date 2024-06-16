*this readme is written in both English and Thai*<br>
*readme นี้เขียนทั้งภาษาอังกฤษและไทย*
# Important API (Partial)

- Due to unclear requirements, only essential parts are documented, avoiding unnecessary details.
- Default database used is sqlite3, which is Django's default, with sample data provided.
- Default permission set to AllowAny.

## Drug
- GET /drug
    - Used to fetch all drug information.
- POST /drug
    - Used to add drug information.

## Patient
- GET /patient
    - Used to fetch all patient information.
- POST /patient
    - Used to add patient information.

### Patient Treatment
- GET /patient/{id}/treatment
    - Used to fetch treatment information for a specific patient by id.
- POST /patient/{id}/treatment
    - Used to add treatment information for a specific patient by id.

## Treatment
- GET /patient/treatment
    - Used to fetch all treatment information.
- POST /patient/treatment
    - Used to add treatment information.

# API สำคัญ(บางส่วน)
- เนื่องจาก requirements ไม่ชัดเจน จึงเลือกเขียนเฉพาะส่วนที่คิดว่าสำคัญ และไม่มากเกินความจำเป็น<br>
- Database ที่ใช้คือ sqlite3 ซึ่งเป็น default ของ django และเพิ่มข้อมูลตัวอย่างไว้แล้ว<br>
- Permission ตั้ง default ไว้ที่ AllowAny
## Drug
- GET /drug
    - ใช้สำหรับดึงข้อมูลของยาทั้งหมด
- POST /drug
    - ใช้สำหรับเพิ่มข้อมูลของยา
## Patient
- GET /patient
    - ใช้สำหรับดึงข้อมูลของผู้ป่วยทั้งหมด
- POST /patient
    - ใช้สำหรับเพิ่มข้อมูลของผู้ป่วย
### Patient Treatment
- GET /patient/{id}/treatment
    - ใช้สำหรับดึงข้อมูลการรักษาของผู้ป่วยตาม id
- POST /patient/{id}/treatment
    - ใช้สำหรับเพิ่มข้อมูลการรักษาของผู้ป่วยตาม id
## Treatment
- GET /patient/treatment
    - ใช้สำหรับดึงข้อมูลการรักษาทั้งหมด
- POST /patient/treatment
    - ใช้สำหรับเพิ่มข้อมูลการรักษา

