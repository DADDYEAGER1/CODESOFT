import json
import os
from PIL import Image
from pathlib import Path

# ========== CONFIGURATION ==========
SOURCE_FOLDER = r"C:\Users\gaurav verma\Downloads\download"
OUTPUT_FOLDER = r"C:\Users\gaurav verma\Mirelle baby\mirelle-site\public\images\hero"
JSON_CONFIG = r"C:\Users\gaurav verma\static filles for scripts\heroimage.json"

# ========== FUNCTIONS ==========

def upscale_image(img, max_scale=4):
    """Upscale image to maximum quality using Lanczos resampling"""
    original_size = img.size
    new_size = (original_size[0] * max_scale, original_size[1] * max_scale)
    print(f"   📈 Upscaling from {original_size} to {new_size}")
    return img.resize(new_size, Image.Resampling.LANCZOS)


def smart_crop_to_aspect_ratio(img, target_ratio):
    """
    Intelligently crop image to target aspect ratio (center-focused)
    target_ratio format: "16:9" or "9:16"
    """
    # Parse aspect ratio
    width_ratio, height_ratio = map(int, target_ratio.split(':'))
    target_aspect = width_ratio / height_ratio
    
    # Current image dimensions
    img_width, img_height = img.size
    current_aspect = img_width / img_height
    
    print(f"   🎯 Target aspect ratio: {target_ratio} ({target_aspect:.2f})")
    print(f"   📐 Current aspect ratio: {current_aspect:.2f}")
    
    if abs(current_aspect - target_aspect) < 0.01:
        print(f"   ✅ Already correct aspect ratio!")
        return img
    
    # Calculate new dimensions
    if current_aspect > target_aspect:
        # Image is too wide, crop width
        new_width = int(img_height * target_aspect)
        new_height = img_height
        left = (img_width - new_width) // 2
        top = 0
        right = left + new_width
        bottom = img_height
    else:
        # Image is too tall, crop height
        new_width = img_width
        new_height = int(img_width / target_aspect)
        left = 0
        top = (img_height - new_height) // 2
        right = img_width
        bottom = top + new_height
    
    print(f"   ✂️ Cropping to {new_width}x{new_height}")
    return img.crop((left, top, right, bottom))


def convert_to_webp(img, output_path, quality=90):
    """Convert image to WebP with high quality"""
    print(f"   💾 Saving as WebP (quality={quality})")
    img.save(output_path, 'WEBP', quality=quality, method=6)
    file_size = os.path.getsize(output_path) / 1024 / 1024  # MB
    print(f"   ✅ Saved: {file_size:.2f} MB")


def process_images():
    """Main processing function"""
    
    # Create output folder if doesn't exist
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    
    # Load JSON configuration
    print(f"📖 Reading config from: {JSON_CONFIG}\n")
    with open(JSON_CONFIG, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    # Get all image files from source folder
    source_images = list(Path(SOURCE_FOLDER).glob('*.*'))
    image_extensions = {'.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff'}
    source_images = [img for img in source_images if img.suffix.lower() in image_extensions]
    
    if not source_images:
        print(f"❌ No images found in {SOURCE_FOLDER}")
        return
    
    print(f"🖼️ Found {len(source_images)} images in source folder")
    print(f"📋 Processing {len(config['images'])} configurations\n")
    print("=" * 80)
    
    # Process each configuration
    for idx, img_config in enumerate(config['images'], 1):
        output_filename = img_config['filename']
        aspect_ratio = img_config['aspect_ratio']
        source_file = img_config.get('source_image', source_images[0].name)
        
        print(f"\n[{idx}/{len(config['images'])}] Processing: {output_filename}")
        print(f"   📁 Source: {source_file}")
        print(f"   📐 Aspect Ratio: {aspect_ratio}")
        
        # Find source image
        source_path = Path(SOURCE_FOLDER) / source_file
        if not source_path.exists():
            # Try to find by index if name doesn't match
            if idx - 1 < len(source_images):
                source_path = source_images[idx - 1]
                print(f"   ⚠️ Using: {source_path.name}")
            else:
                print(f"   ❌ Source image not found, skipping...")
                continue
        
        try:
            # Load image
            img = Image.open(source_path)
            print(f"   📥 Loaded: {img.size[0]}x{img.size[1]} ({img.format})")
            
            # Convert to RGB if necessary
            if img.mode in ('RGBA', 'LA', 'P'):
                print(f"   🎨 Converting {img.mode} to RGB")
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                img = background
            
            # Step 1: Upscale to maximum quality
            img = upscale_image(img, max_scale=4)
            
            # Step 2: Smart crop to aspect ratio
            img = smart_crop_to_aspect_ratio(img, aspect_ratio)
            
            # Step 3: Convert to WebP
            output_path = os.path.join(OUTPUT_FOLDER, output_filename)
            convert_to_webp(img, output_path, quality=92)
            
            print(f"   🎉 SUCCESS: {output_filename}")
            
        except Exception as e:
            print(f"   ❌ ERROR: {str(e)}")
            continue
    
    print("\n" + "=" * 80)
    print("✅ All images processed!")
    print(f"📂 Output folder: {OUTPUT_FOLDER}")


# ========== MAIN EXECUTION ==========
if __name__ == "__main__":
    print("🚀 Starting Image Upscaler & WebP Converter\n")
    process_images()