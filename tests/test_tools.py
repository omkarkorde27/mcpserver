"""
Unit tests for MCP tool functions.

These test the tool functions directly (not via MCP protocol).
Run with: python -m pytest tests/test_tools.py -v
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server import get_program_links, get_contact_info
from schools import FALLBACK_URL


class TestGetProgramLinks:
    """Tests for the get_program_links tool."""

    def test_known_school_returns_url(self):
        result = get_program_links("Luddy")
        assert "luddy.indiana.edu" in result
        assert "Luddy School" in result

    def test_kelley_returns_program_url(self):
        result = get_program_links("Kelley")
        assert "kelley.iu.edu/programs" in result

    def test_unknown_school_returns_fallback(self):
        result = get_program_links("Unknown School")
        assert FALLBACK_URL in result
        assert "Could not identify" in result

    def test_keyword_match(self):
        result = get_program_links("Data Science")
        assert "luddy.indiana.edu" in result

    def test_multiple_schools(self):
        result = get_program_links("Luddy and Kelley")
        assert "luddy.indiana.edu" in result
        assert "kelley.iu.edu" in result

    def test_all_schools_return_valid_urls(self):
        school_keywords = [
            "Hamilton Lugar", "Luddy", "Kelley", "Arts and Sciences",
            "Eskenazi", "Jacobs", "Maurer", "O'Neill", "Education",
            "Medicine", "Nursing", "Optometry", "Public Health",
            "Social Work", "Media School",
        ]
        for keyword in school_keywords:
            result = get_program_links(keyword)
            assert "https://" in result, f"No URL in result for '{keyword}': {result}"
            assert "Could not identify" not in result, \
                f"Failed to match '{keyword}': {result}"


class TestGetContactInfo:
    """Tests for the get_contact_info tool."""

    def test_known_school_returns_contact_url(self):
        result = get_contact_info("Luddy")
        assert "luddy.iu.edu/about/contact" in result
        assert "Luddy School" in result

    def test_kelley_returns_contact_url(self):
        result = get_contact_info("Kelley")
        assert "kelley.iu.edu/about/contact" in result

    def test_unknown_school_returns_fallback(self):
        result = get_contact_info("Unknown School")
        assert FALLBACK_URL in result
        assert "Could not identify" in result

    def test_keyword_match_admissions(self):
        result = get_contact_info("MBA")
        assert "kelley.iu.edu" in result

    def test_multiple_schools_contact(self):
        result = get_contact_info("Luddy and Kelley")
        assert "luddy.iu.edu" in result
        assert "kelley.iu.edu" in result

    def test_all_schools_return_contact_urls(self):
        school_keywords = [
            "Hamilton Lugar", "Luddy", "Kelley", "Arts and Sciences",
            "Eskenazi", "Jacobs", "Maurer", "O'Neill", "Education",
            "Medicine", "Nursing", "Optometry", "Public Health",
            "Social Work", "Media School",
        ]
        for keyword in school_keywords:
            result = get_contact_info(keyword)
            assert "https://" in result, f"No URL in result for '{keyword}': {result}"
            assert "Could not identify" not in result, \
                f"Failed to match '{keyword}': {result}"
