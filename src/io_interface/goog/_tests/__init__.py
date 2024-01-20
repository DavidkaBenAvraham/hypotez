from pathlib import Path
abs_path = Path(__file__).parent.parent.parent.absolute()
print(f'absolute path {abs_path}')
import sys
sys.path.append(abs_path)
