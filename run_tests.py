#!/usr/bin/env python3
"""
Test runner for Library Manager project
"""

import unittest
import sys
import os

# Test papkasini qo'shish
sys.path.insert(0, os.path.abspath('.'))


def run_tests():
    """Barcha testlarni ishga tushiradi"""
    print("🧪 Library Manager testlari ishga tushirilmoqda...")
    print("=" * 50)

    # Test papkasini topish
    test_dir = 'tests'
    if not os.path.exists(test_dir):
        print(f"❌ {test_dir} papkasi topilmadi!")
        return False

    # Test fayllarini topish
    test_files = []
    for file in os.listdir(test_dir):
        if file.startswith('test_') and file.endswith('.py'):
            test_files.append(os.path.join(test_dir, file))

    if not test_files:
        print("❌ Test fayllari topilmadi!")
        return False

    print(f"📁 {len(test_files)} ta test fayli topildi:")
    for file in test_files:
        print(f"   - {file}")

    print("\n" + "=" * 50)

    # Testlarni ishga tushirish
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    for test_file in test_files:
        # Test faylini import qilish
        module_name = os.path.splitext(os.path.basename(test_file))[0]
        try:
            # Test faylini yuklash
            import importlib.util
            spec = importlib.util.spec_from_file_location(
                module_name, test_file)
            if spec is not None and spec.loader is not None:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
            else:
                print(f"❌ {test_file} faylini yuklashda xatolik")
                continue

            # Test klasslarini topish
            for name in dir(module):
                obj = getattr(module, name)
                if isinstance(obj, type) and issubclass(obj, unittest.TestCase):
                    tests = loader.loadTestsFromTestCase(obj)
                    suite.addTests(tests)
                    print(f"✅ {name} test klassi qo'shildi")

        except Exception as e:
            print(f"❌ {test_file} faylini yuklashda xatolik: {e}")

    # Testlarni ishga tushirish
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 50)
    print("📊 Test natijalari:")
    print(
        f"   ✅ Muvaffaqiy: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"   ❌ Xatoliklar: {len(result.failures)}")
    print(f"   ⚠️  Xatolar: {len(result.errors)}")
    print(f"   📊 Jami: {result.testsRun}")

    if result.failures:
        print("\n❌ Muvaffaqiy bo'lmagan testlar:")
        for test, traceback in result.failures:
            print(f"   - {test}")

    if result.errors:
        print("\n⚠️  Xatolar:")
        for test, traceback in result.errors:
            print(f"   - {test}")

    return len(result.failures) == 0 and len(result.errors) == 0


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
