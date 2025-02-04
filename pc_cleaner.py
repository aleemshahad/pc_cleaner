import os
import shutil
import winreg
import logging
from datetime import datetime
import ctypes

class PCCleaner:
    def __init__(self):
        self.cleaned_files = 0
        self.cleaned_size = 0
        self.setup_logging()
        
    def setup_logging(self):
        logging.basicConfig(
            filename='cleaner_log.txt',
            level=logging.INFO,
            format='%(asctime)s - %(message)s'
        )
    
    def get_temp_folders(self):
        """Get common Windows temporary folders"""
        temp_locations = []
        # Windows Temp folder
        temp_locations.append(os.environ.get('TEMP'))
        # Windows Prefetch
        temp_locations.append(os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Prefetch'))
        # Windows temporary files
        temp_locations.append(os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Temp'))
        return temp_locations

    def is_admin(self):
        """Check if the script is running with admin privileges"""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def clean_directory(self, directory):
        """Clean a specific directory"""
        if not os.path.exists(directory):
            return

        for root, dirs, files in os.walk(directory, topdown=False):
            # Remove files
            for name in files:
                try:
                    file_path = os.path.join(root, name)
                    file_size = os.path.getsize(file_path)
                    os.remove(file_path)
                    self.cleaned_files += 1
                    self.cleaned_size += file_size
                    logging.info(f"Removed file: {file_path}")
                except Exception as e:
                    logging.error(f"Error removing file {name}: {str(e)}")

            # Remove empty directories
            for name in dirs:
                try:
                    dir_path = os.path.join(root, name)
                    os.rmdir(dir_path)
                    logging.info(f"Removed empty directory: {dir_path}")
                except Exception as e:
                    logging.error(f"Error removing directory {name}: {str(e)}")

    def format_size(self, size):
        """Convert bytes to human readable format"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024
        return f"{size:.2f} TB"

    def clean_system(self):
        """Main cleaning function"""
        if not self.is_admin():
            print("Warning: Running without administrator privileges. Some files may not be accessible.")
            logging.warning("Script running without administrator privileges")

        print("Starting PC Cleanup...")
        logging.info("Starting cleanup process")

        # Clean each temp location
        for folder in self.get_temp_folders():
            if folder and os.path.exists(folder):
                print(f"Cleaning {folder}...")
                self.clean_directory(folder)

        # Print summary
        print("\nCleanup Summary:")
        print(f"Total files removed: {self.cleaned_files}")
        print(f"Total space freed: {self.format_size(self.cleaned_size)}")
        logging.info(f"Cleanup completed. Removed {self.cleaned_files} files, freed {self.format_size(self.cleaned_size)}")

if __name__ == "__main__":
    cleaner = PCCleaner()
    cleaner.clean_system()
