"""
Unit tests for school matching logic.

Run with: python -m pytest tests/test_matching.py -v
"""

import sys
import os

# Add parent directory to path so we can import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from matching import find_school, find_multiple_schools
from schools import SCHOOLS


class TestFindSchool:
    """Tests for the find_school function."""

    # --- Exact keyword matches ---

    def test_luddy_by_name(self):
        result = find_school("Luddy")
        assert result is not None
        assert result["id"] == "luddy"

    def test_kelley_by_name(self):
        result = find_school("Kelley")
        assert result is not None
        assert result["id"] == "kelley"

    def test_oneill_by_name(self):
        result = find_school("O'Neill")
        assert result is not None
        assert result["id"] == "oneill"

    def test_oneill_without_apostrophe(self):
        result = find_school("ONeill")
        assert result is not None
        assert result["id"] == "oneill"

    def test_hamilton_lugar_by_name(self):
        result = find_school("Hamilton Lugar")
        assert result is not None
        assert result["id"] == "hamilton_lugar"

    def test_maurer_by_name(self):
        result = find_school("Maurer")
        assert result is not None
        assert result["id"] == "maurer"

    # --- Keyword matches ---

    def test_luddy_by_data_science(self):
        result = find_school("Data Science")
        assert result is not None
        assert result["id"] == "luddy"

    def test_kelley_by_mba(self):
        result = find_school("MBA")
        assert result is not None
        assert result["id"] == "kelley"

    def test_kelley_by_business(self):
        result = find_school("Business")
        assert result is not None
        assert result["id"] == "kelley"

    def test_maurer_by_law(self):
        result = find_school("Law")
        assert result is not None
        assert result["id"] == "maurer"

    def test_jacobs_by_music(self):
        result = find_school("Music")
        assert result is not None
        assert result["id"] == "jacobs"

    def test_public_health_by_mph(self):
        result = find_school("MPH")
        assert result is not None
        assert result["id"] == "public_health"

    def test_social_work_by_msw(self):
        result = find_school("MSW")
        assert result is not None
        assert result["id"] == "social_work"

    def test_media_by_journalism(self):
        result = find_school("Journalism")
        assert result is not None
        assert result["id"] == "media"

    def test_nursing_by_keyword(self):
        result = find_school("Nursing")
        assert result is not None
        assert result["id"] == "nursing"

    def test_optometry_by_vision(self):
        result = find_school("Vision Science")
        assert result is not None
        assert result["id"] == "optometry"

    def test_education_by_teaching(self):
        result = find_school("Teaching")
        assert result is not None
        assert result["id"] == "education"

    def test_medicine_by_medical(self):
        result = find_school("Medical")
        assert result is not None
        assert result["id"] == "medicine"

    def test_eskenazi_by_architecture(self):
        result = find_school("Architecture")
        assert result is not None
        assert result["id"] == "eskenazi"

    def test_hls_by_international(self):
        result = find_school("International")
        assert result is not None
        assert result["id"] == "hamilton_lugar"

    # --- Case insensitivity ---

    def test_case_insensitive_luddy(self):
        result = find_school("luddy")
        assert result is not None
        assert result["id"] == "luddy"

    def test_case_insensitive_kelley_upper(self):
        result = find_school("KELLEY")
        assert result is not None
        assert result["id"] == "kelley"

    def test_case_insensitive_mixed(self):
        result = find_school("data science")
        assert result is not None
        assert result["id"] == "luddy"

    # --- Query within longer string ---

    def test_school_in_sentence(self):
        result = find_school("I want to know about Luddy programs")
        assert result is not None
        assert result["id"] == "luddy"

    def test_keyword_in_sentence(self):
        result = find_school("Tell me about the MBA program")
        assert result is not None
        assert result["id"] == "kelley"

    # --- No match / edge cases ---

    def test_no_match_returns_none(self):
        result = find_school("Underwater Basket Weaving")
        assert result is None

    def test_empty_string_returns_none(self):
        result = find_school("")
        assert result is None

    def test_whitespace_only_returns_none(self):
        result = find_school("   ")
        assert result is None

    def test_none_input_returns_none(self):
        result = find_school(None)
        assert result is None

    # --- Disambiguation (Public Health vs Public Affairs) ---

    def test_public_health_not_oneill(self):
        result = find_school("Public Health")
        assert result is not None
        assert result["id"] == "public_health"

    def test_public_affairs_not_public_health(self):
        result = find_school("Public Affairs")
        assert result is not None
        assert result["id"] == "oneill"

    # --- All 15 schools have required fields ---

    def test_all_schools_have_required_fields(self):
        for school in SCHOOLS:
            assert "id" in school, f"Missing id for {school}"
            assert "full_name" in school, f"Missing full_name for {school['id']}"
            assert "keywords" in school, f"Missing keywords for {school['id']}"
            assert "program_url" in school, f"Missing program_url for {school['id']}"
            assert "contact_url" in school, f"Missing contact_url for {school['id']}"
            assert len(school["keywords"]) > 0, f"Empty keywords for {school['id']}"

    def test_fifteen_schools_exist(self):
        assert len(SCHOOLS) == 15

    def test_all_urls_start_with_https(self):
        for school in SCHOOLS:
            assert school["program_url"].startswith("https://"), \
                f"program_url for {school['id']} doesn't start with https://"
            assert school["contact_url"].startswith("https://"), \
                f"contact_url for {school['id']} doesn't start with https://"


class TestFindMultipleSchools:
    """Tests for the find_multiple_schools function."""

    def test_single_school(self):
        results = find_multiple_schools("Luddy")
        assert len(results) == 1
        assert results[0]["id"] == "luddy"

    def test_two_schools(self):
        results = find_multiple_schools("Compare Luddy and Kelley")
        assert len(results) == 2
        ids = {s["id"] for s in results}
        assert "luddy" in ids
        assert "kelley" in ids

    def test_no_match(self):
        results = find_multiple_schools("random nonsense")
        assert len(results) == 0

    def test_empty_string(self):
        results = find_multiple_schools("")
        assert len(results) == 0

    def test_none_input(self):
        results = find_multiple_schools(None)
        assert len(results) == 0

    def test_no_duplicates(self):
        # "Luddy Informatics Computing" should still return Luddy only once
        results = find_multiple_schools("Luddy Informatics Computing")
        luddy_count = sum(1 for s in results if s["id"] == "luddy")
        assert luddy_count == 1
