import os
from PIL import Image

def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

def compress_images_in_dir(directory, max_dimension=1200, quality=82):
    count = 0
    print(f"Buscando imagens em {directory}...")
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            # Filter non-image or specific formats
            ext = os.path.splitext(file)[1].lower()
            if ext in ['.jpg', '.jpeg', '.png']:
                try:
                    with Image.open(filepath) as img:
                        # Skip if it's already small enough and size is OK
                        if img.width <= max_dimension and img.height <= max_dimension and os.path.getsize(filepath) < 300 * 1024:
                            # small files under 300kb are skipped
                            pass
                        
                        # Apply resizing
                        img_format = img.format # Retain the format
                        
                        # Convert RGBA to RGB for JPEG if needed
                        if ext in ['.jpg', '.jpeg'] and img.mode in ('RGBA', 'P'):
                            img = img.convert('RGB')
                            
                        # Resize proportionally
                        if img.width > max_dimension or img.height > max_dimension:
                            ratio = min(max_dimension / img.width, max_dimension / img.height)
                            new_size = (int(img.width * ratio), int(img.height * ratio))
                            img = img.resize(new_size, Image.Resampling.LANCZOS)
                            
                        # Save
                        if ext in ['.jpg', '.jpeg']:
                            img.save(filepath, 'JPEG', quality=quality, optimize=True)
                            count += 1
                        elif ext == '.png':
                            img.save(filepath, 'PNG', optimize=True)
                            count += 1
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")
    print(f"Processed {count} images in {directory}")

if __name__ == "__main__":
    start_size = get_size('foto')
    print(f"Tamanho original: {start_size / (1024*1024):.2f} MB")
    
    compress_images_in_dir('foto')
    
    end_size = get_size('foto')
    print(f"Tamanho final: {end_size / (1024*1024):.2f} MB")
    print(f"Redução de: {start_size/(1024*1024) - end_size/(1024*1024):.2f} MB")
