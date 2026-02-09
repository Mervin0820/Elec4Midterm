import os
import cv2
import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from candid_or_posed import (
    load_images,
    classify_candid_or_posed,
    save_image
)

INPUT_DIR = "input"

@pytest.fixture
def input_images():

    assert os.path.exists(INPUT_DIR), "input/ folder does not exist in repo"

    files = [
        f for f in os.listdir(INPUT_DIR)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ]

    assert len(files) > 0, "No images found in input/ folder"
    return files


@pytest.fixture
def output_dir():

    out = Path("output")
    out.mkdir(parents=True, exist_ok=True)
    return out


def test_images_load_correctly(input_images):

    loaded = list(load_images(INPUT_DIR, input_images))

    assert len(loaded) > 0

    for name, img in loaded:
        assert img is not None, f"Failed to load {name}"
        assert img.size > 0, f"Empty image: {name}"

def test_classification_runs_on_all_images(input_images):

    for name, img in load_images(INPUT_DIR, input_images):
        label, score, blur = classify_candid_or_posed(img)

        assert label in {"CANDID", "POSED"}
        assert isinstance(score, int)
        assert isinstance(blur, float)

def test_output_images_are_saved(output_dir, input_images):

    for name, img in load_images(INPUT_DIR, input_images):
        label, _, _ = classify_candid_or_posed(img)

        cv2.putText(
            img,
            label,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )

        saved_path = save_image(str(output_dir), name, img)
        assert os.path.exists(saved_path), f"Output not saved for {name}"

def test_classified_image_is_modified(output_dir, input_images):

    for name in input_images:
        original_path = os.path.join(INPUT_DIR, name)
        original_img = cv2.imread(original_path)
        assert original_img is not None, f"Failed to read {name}"

        original_copy = original_img.copy()

        label, _, _ = classify_candid_or_posed(original_img)

        cv2.putText(
            original_img,
            label,
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            2,
            (255, 0, 0),
            2
        )

        saved_path = save_image(str(output_dir), name, original_img)
        saved_img = cv2.imread(saved_path)
        assert saved_img is not None, f"Failed to reload saved image {name}"

        diff = cv2.absdiff(original_copy, saved_img)
        assert diff.sum() > 0, f"Classified image {name} was not modified"