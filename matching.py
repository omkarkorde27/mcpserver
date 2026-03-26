"""
School matching logic.
Maps user input (school name, keyword, program name) to the correct
school dictionary from the SCHOOLS list.
"""

import re
from schools import SCHOOLS


def _keyword_matches(keyword: str, query: str) -> bool:
    """Check if a keyword matches in the query using word boundary matching.

    Multi-word keywords (e.g. "Data Science", "Public Health") use
    simple substring matching since they're specific enough.

    Short keywords and acronyms (e.g. "MBA", "CS", "MSW") use word
    boundary matching to avoid false positives like "CoMPAre" matching "MPA".

    Args:
        keyword: The keyword to search for (already lowered by caller).
        query: The query string to search in (already lowered by caller).

    Returns:
        True if the keyword matches in the query.
    """
    if " " in keyword:
        # Multi-word keywords: substring match is safe
        return keyword in query
    else:
        # Single-word/acronym: use word boundary to avoid partial matches
        # e.g. "mpa" should not match inside "compare"
        pattern = r'\b' + re.escape(keyword) + r'\b'
        return bool(re.search(pattern, query))


def find_school(query: str):
    """Match a query string to a school using keyword matching.

    Performs case-insensitive matching against each school's keyword list.
    Returns the first matching school dict, or None if no match found.

    Args:
        query: A string that might contain a school name or keyword.
               e.g. "Luddy", "Data Science", "Kelley MBA"

    Returns:
        dict: The matching school dictionary, or None.
    """
    if not query or not query.strip():
        return None

    query_lower = query.lower().strip()

    # Longer keywords are checked first to avoid partial matches
    # e.g. "Public Health" should match before "Public" (which could match O'Neill)
    for school in sorted(SCHOOLS, key=lambda s: max(len(k) for k in s["keywords"]), reverse=True):
        for keyword in school["keywords"]:
            if _keyword_matches(keyword.lower(), query_lower):
                return school

    return None


def find_multiple_schools(query: str):
    """Match a query string that may reference multiple schools.

    Useful for comparison queries like "Compare Luddy and Kelley".

    Args:
        query: A string that might contain multiple school references.

    Returns:
        list: A list of matching school dictionaries (may be empty).
    """
    if not query or not query.strip():
        return []

    query_lower = query.lower().strip()
    matched = []
    matched_ids = set()

    for school in sorted(SCHOOLS, key=lambda s: max(len(k) for k in s["keywords"]), reverse=True):
        for keyword in school["keywords"]:
            if _keyword_matches(keyword.lower(), query_lower) and school["id"] not in matched_ids:
                matched.append(school)
                matched_ids.add(school["id"])
                break

    return matched
