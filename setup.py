#!/usr/bin/env python3
"""
Setup script for 100 Days DSA Course

This script helps you set up your development environment
and verify everything is working correctly.

Usage: python setup.py
"""

import sys
import subprocess
import os
from pathlib import Path


def check_python_version():
    """Check if Python version is 3.8 or higher."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
        print("   Please upgrade Python from https://python.org")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
    return True


def install_requirements():
    """Install required packages from requirements.txt."""
    try:
        print("📦 Installing required packages...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ All packages installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install packages")
        print("   You can install manually with: pip install -r requirements.txt")
        return False
    except FileNotFoundError:
        print("⚠️  requirements.txt not found - skipping package installation")
        return True


def create_personal_folder():
    """Create a personal folder for user's solutions."""
    personal_dir = Path("my_solutions")
    if not personal_dir.exists():
        personal_dir.mkdir()
        print(f"✅ Created {personal_dir} folder for your personal solutions")
        
        # Create a sample file
        sample_file = personal_dir / "notes.md"
        with open(sample_file, "w") as f:
            f.write("# My DSA Journey Notes\n\n")
            f.write("## Day 1\n")
            f.write("- [Your notes here]\n\n")
            f.write("## Patterns I've Learned\n")
            f.write("- Two pointers\n")
            f.write("- [Add more as you learn]\n\n")
            f.write("## Problems to Review\n")
            f.write("- [Add problems you want to revisit]\n")
        
        print(f"✅ Created sample notes file: {sample_file}")
    else:
        print(f"✅ {personal_dir} folder already exists")
    
    return True


def test_day_1():
    """Test that Day 1 solution works."""
    try:
        # Add the day_01 directory to path
        day_01_path = Path("day_01")
        if day_01_path.exists():
            sys.path.insert(0, str(day_01_path))
            
            # Import and test the solution
            from solution import two_sum
            
            # Run a quick test
            result = two_sum([2, 7, 11, 15], 9)
            expected = [0, 1]
            
            if result == expected:
                print("✅ Day 1 solution works correctly")
                return True
            else:
                print(f"❌ Day 1 test failed: expected {expected}, got {result}")
                return False
        else:
            print("⚠️  Day 1 folder not found - skipping test")
            return True
            
    except Exception as e:
        print(f"❌ Error testing Day 1: {e}")
        return False
    finally:
        # Clean up the path
        if str(day_01_path) in sys.path:
            sys.path.remove(str(day_01_path))


def show_next_steps():
    """Show user what to do next."""
    print("\n" + "="*60)
    print("🎉 SETUP COMPLETE!")
    print("="*60)
    print()
    print("📚 Next Steps:")
    print("1. Read the main README.md for course overview")
    print("2. Check out QUICK_START.md for daily routine")
    print("3. Navigate to day_01/ and start your journey!")
    print("4. Join our community (links in RESOURCES.md)")
    print()
    print("🚀 Quick Start Commands:")
    print("   cd day_01")
    print("   python solution.py    # See the solution in action")
    print("   python test.py        # Run comprehensive tests")
    print()
    print("💡 Tips:")
    print("• Start each day by reading the README.md")
    print("• Try solving before looking at the solution")
    print("• Use my_solutions/ folder for your own attempts")
    print("• Take notes and track your progress")
    print()
    print("🎯 Remember: Consistency beats intensity!")
    print("   1 hour daily >> 7 hours once a week")
    print()
    print("Good luck on your 100-day journey! 🚀")


def run_setup():
    """Run the complete setup process."""
    print("🔧 100 DAYS DSA COURSE SETUP")
    print("="*60)
    print()
    
    success = True
    
    # Check Python version
    if not check_python_version():
        success = False
    
    # Install requirements
    if success and not install_requirements():
        success = False
    
    # Create personal folder
    if success and not create_personal_folder():
        success = False
    
    # Test Day 1
    if success and not test_day_1():
        success = False
    
    print("\n" + "="*60)
    
    if success:
        print("✅ Setup completed successfully!")
        show_next_steps()
    else:
        print("❌ Setup encountered some issues")
        print("   Please check the error messages above")
        print("   You can still start the course manually")
        print("   See QUICK_START.md for manual setup instructions")


if __name__ == "__main__":
    run_setup()
