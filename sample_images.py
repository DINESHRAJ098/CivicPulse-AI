"""
Generates visual civic benchmark images for demo testing
"""

import os
from PIL import Image, ImageDraw, ImageFont

def create_sample_assets(output_dir="samples"):
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Pothole
    img1 = Image.new("RGB", (600, 400), color=(60, 60, 65))
    draw1 = ImageDraw.Draw(img1)
    # Road texture & lines
    for y in range(0, 400, 20):
        draw1.line([(0, y), (600, y)], fill=(55, 55, 60), width=1)
    # Yellow road center divider dashes
    for x in range(30, 600, 70):
        draw1.rectangle([x, 195, x + 40, 205], fill=(230, 190, 40))
    # Pothole crater
    draw1.ellipse([210, 130, 430, 290], fill=(25, 20, 18), outline=(90, 80, 70), width=5)
    draw1.ellipse([240, 150, 400, 270], fill=(15, 12, 10))
    # Cracks branching out
    draw1.line([(210, 200), (150, 180), (110, 210)], fill=(30, 30, 30), width=3)
    draw1.line([(430, 220), (490, 210), (540, 240)], fill=(30, 30, 30), width=3)
    draw1.line([(310, 130), (330, 80), (360, 50)], fill=(30, 30, 30), width=3)
    # Caption label
    draw1.rectangle([20, 20, 240, 55], fill=(0, 0, 0, 180))
    draw1.text((30, 28), "CIVIC SCAN: SEVERE POTHOLE", fill=(255, 255, 255))
    img1.save(os.path.join(output_dir, "pothole_severe.jpg"))

    # 2. Water Pipeline Leak / Flooding
    img2 = Image.new("RGB", (600, 400), color=(70, 75, 70))
    draw2 = ImageDraw.Draw(img2)
    # Pavement & curb
    draw2.rectangle([0, 0, 600, 150], fill=(130, 130, 130))
    draw2.line([(0, 150), (600, 150)], fill=(50, 50, 50), width=4)
    # Flooded puddle
    draw2.ellipse([100, 170, 520, 370], fill=(35, 95, 160), outline=(60, 140, 210), width=4)
    # Burst pipe water gush
    draw2.ellipse([280, 230, 360, 310], fill=(120, 190, 255), outline=(200, 230, 255), width=3)
    draw2.line([(320, 270), (250, 200)], fill=(220, 240, 255), width=4)
    draw2.line([(320, 270), (390, 210)], fill=(220, 240, 255), width=4)
    draw2.rectangle([20, 20, 260, 55], fill=(0, 0, 0, 180))
    draw2.text((30, 28), "CIVIC SCAN: PIPELINE BURST", fill=(255, 255, 255))
    img2.save(os.path.join(output_dir, "water_pipeline_burst.jpg"))

    # 3. Waste Overflow
    img3 = Image.new("RGB", (600, 400), color=(110, 105, 95))
    draw3 = ImageDraw.Draw(img3)
    # Brick wall background
    draw3.rectangle([0, 0, 600, 180], fill=(150, 80, 70))
    # Green municipal bin
    draw3.rectangle([180, 120, 420, 320], fill=(20, 110, 45), outline=(10, 60, 20), width=4)
    # Garbage pile spilling out
    draw3.ellipse([140, 250, 460, 380], fill=(80, 75, 60))
    draw3.polygon([(180, 120), (280, 60), (380, 110), (420, 120)], fill=(180, 170, 130))
    # Plastic bags and bottles
    draw3.rectangle([160, 310, 210, 340], fill=(210, 50, 50))
    draw3.rectangle([380, 300, 440, 330], fill=(40, 120, 220))
    draw3.ellipse([270, 330, 320, 360], fill=(230, 230, 80))
    draw3.rectangle([20, 20, 260, 55], fill=(0, 0, 0, 180))
    draw3.text((30, 28), "CIVIC SCAN: GARBAGE OVERFLOW", fill=(255, 255, 255))
    img3.save(os.path.join(output_dir, "waste_overflow.jpg"))

    # 4. Electrical Hazard
    img4 = Image.new("RGB", (600, 400), color=(30, 35, 50))
    draw4 = ImageDraw.Draw(img4)
    # Electric pole
    draw4.rectangle([280, 0, 315, 400], fill=(90, 95, 105), outline=(50, 55, 65), width=3)
    draw4.line([(200, 60), (400, 60)], fill=(90, 95, 105), width=8)
    # Hanging broken wire sparking
    draw4.line([(290, 60), (260, 180), (220, 270)], fill=(20, 20, 25), width=4)
    # Bright electric spark at dangling tip
    draw4.ellipse([200, 255, 240, 285], fill=(255, 255, 150), outline=(255, 160, 30), width=4)
    draw4.line([(220, 270), (180, 240)], fill=(255, 255, 200), width=2)
    draw4.line([(220, 270), (250, 230)], fill=(255, 255, 200), width=2)
    draw4.line([(220, 270), (190, 300)], fill=(255, 255, 200), width=2)
    draw4.rectangle([20, 20, 280, 55], fill=(0, 0, 0, 180))
    draw4.text((30, 28), "CIVIC SCAN: LIVE CABLE HAZARD", fill=(255, 255, 255))
    img4.save(os.path.join(output_dir, "electrical_hazard.jpg"))

    # 5. Repaired Road (Resolution Verification Demo)
    img5 = Image.new("RGB", (600, 400), color=(60, 60, 65))
    draw5 = ImageDraw.Draw(img5)
    # Freshly laid dark smooth bitumen patch
    draw5.rectangle([180, 110, 450, 300], fill=(30, 30, 32), outline=(50, 50, 55), width=3)
    # Fresh road line
    for x in range(30, 600, 70):
        draw5.rectangle([x, 195, x + 40, 205], fill=(240, 200, 40))
    draw5.rectangle([20, 20, 290, 55], fill=(10, 80, 30, 200))
    draw5.text((30, 28), "VERIFIED REPAIR: FRESH BITUMEN", fill=(255, 255, 255))
    img5.save(os.path.join(output_dir, "repaired_road_success.jpg"))
    
    print("Sample civic assets generated successfully.")

if __name__ == "__main__":
    create_sample_assets()
