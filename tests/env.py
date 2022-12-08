import sys
from pathlib import Path
project_root = Path(__file__).parent.parent.absolute()
sys.path.append(project_root.__str__())