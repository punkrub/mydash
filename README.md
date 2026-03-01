# 📊 Simple Sales Dashboard

โปรเจกต์นี้เป็นการทดลองสร้าง Dashboard อย่างง่ายด้วย Python โดยใช้ไลบรารี Streamlit เพื่อทดสอบความเข้าใจในการแสดงผลข้อมูล (Data Visualization) และการจัดการ Version Control ด้วย Git

## 🚀 ฟีเจอร์ของโปรแกรม
* ใช้ข้อมูลจำลองของยอดขายสินค้าในหมวดหมู่ต่างๆ
* มี Interactive component: สามารถเลือกกรองข้อมูลภูมิภาค (Region) ที่ Sidebar ด้านซ้ายได้ แล้วกราฟจะเปลี่ยนตามข้อมูลที่เลือก
* มีกราฟ 3 รูปแบบ (สร้างด้วย Plotly Express):
    1.  Bar Chart: ยอดขายแบ่งตามหมวดหมู่
    2.  Pie Chart: สัดส่วนกำไร
    3.  Line Chart: แนวโน้มยอดขาย

## 🛠️ วิธีการรันโปรแกรม

1.  โคลนโปรเจกต์นี้ลงเครื่อง (Clone repository)
2.  ติดตั้งไลบรารีที่จำเป็น โดยรันคำสั่ง:
    ```bash
    pip install -r requirements.txt
    ```
3.  รันแอปพลิเคชันด้วยคำสั่ง:
    ```bash
    streamlit run app.py
    ```
4.  โปรแกรมจะเปิดหน้า Dashboard บน Web Browser ของคุณโดยอัตโนมัติ (ปกติจะอยู่ที่ `http://localhost:8501`)