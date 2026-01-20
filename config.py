"""Configuration constants for the eBird hotspot guide."""

from pathlib import Path


def find_ebird_files(data_dir: Path) -> tuple[Path, Path]:
    """
    Auto-detect eBird data files in the given directory.

    Looks for:
    - Main file: ebd_*.txt (excluding *_sampling.txt)
    - Sampling file: *_sampling.txt

    Returns:
        Tuple of (main_file, sampling_file) paths

    Raises:
        FileNotFoundError if files cannot be found
    """
    # Find sampling file
    sampling_files = list(data_dir.glob("*_sampling.txt"))
    if not sampling_files:
        raise FileNotFoundError(
            f"No sampling file (*_sampling.txt) found in {data_dir}"
        )
    if len(sampling_files) > 1:
        raise FileNotFoundError(
            f"Multiple sampling files found in {data_dir}: {sampling_files}"
        )
    sampling_file = sampling_files[0]

    # Find main file (ebd_*.txt but not *_sampling.txt)
    main_files = [
        f for f in data_dir.glob("ebd_*.txt")
        if not f.name.endswith("_sampling.txt")
    ]
    if not main_files:
        raise FileNotFoundError(
            f"No main data file (ebd_*.txt) found in {data_dir}"
        )
    if len(main_files) > 1:
        raise FileNotFoundError(
            f"Multiple main data files found in {data_dir}: {main_files}"
        )
    main_file = main_files[0]

    return main_file, sampling_file


# Paths
DATA_DIR = Path(__file__).parent.parent
OUTPUT_DIR = DATA_DIR / "output"

# Auto-detect data files
MAIN_FILE, SAMPLING_FILE = find_ebird_files(DATA_DIR)

# Processing parameters
CHUNK_SIZE = 100000          # Rows per chunk for main file
SAMPLING_CHUNK_SIZE = 50000  # Rows per chunk for sampling file

# Confidence thresholds
MIN_CHECKLISTS_THRESHOLD = 10   # Minimum checklists to include hotspot
HIGH_CONFIDENCE_MIN = 100       # Checklists for "high" confidence
MEDIUM_CONFIDENCE_MIN = 30      # Checklists for "medium" confidence

# Seasonal definitions (month numbers)
SEASONS = {
    'spring': [3, 4, 5],
    'summer': [6, 7],
    'fall': [8, 9, 10, 11],
    'winter': [12, 1, 2]
}

# Output formatting
JSON_INDENT = 2
RATE_DECIMAL_PLACES = 4

# Columns to read from sampling file
SAMPLING_COLS = [
    'LOCALITY ID',
    'LOCALITY',
    'LOCALITY TYPE',
    'LATITUDE',
    'LONGITUDE',
    'OBSERVATION DATE',
    'SAMPLING EVENT IDENTIFIER',
    'ALL SPECIES REPORTED',
]

# Columns to read from main file
MAIN_COLS = [
    'COMMON NAME',
    'SCIENTIFIC NAME',
    'CATEGORY',
    'LOCALITY ID',
    'LOCALITY TYPE',
    'SAMPLING EVENT IDENTIFIER',
    'ALL SPECIES REPORTED',
    'OBSERVATION DATE',
    'OBSERVATION COUNT',
]
