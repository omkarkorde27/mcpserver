"""
School data for all 15 Indiana University graduate schools.
Each school has a unique ID, full name, keyword triggers, program page URL,
and contact/admissions page URL.

To add a new school: append a new dictionary to the SCHOOLS list.
To update a URL: edit the relevant program_url or contact_url field.
"""

FALLBACK_URL = "https://graduate.indiana.edu/admissions/index.html"

SCHOOLS = [
    {
        "id": "hamilton_lugar",
        "full_name": "Hamilton Lugar School of International Studies",
        "keywords": [
            "Hamilton Lugar", "HLS", "International",
            "Global", "Global Studies", "International Studies",
        ],
        "program_url": "https://hls.indiana.edu/academics/graduate/index.html",
        "contact_url": "https://hls.indiana.edu/about/contact.html",
    },
    {
        "id": "luddy",
        "full_name": "Luddy School of Informatics, Computing, and Engineering",
        "keywords": [
            "Luddy", "Informatics", "Computing", "Data Science",
            "CS", "Computer Science", "HCI", "Bioinformatics",
            "Cybersecurity", "Library Science",
        ],
        "program_url": "https://luddy.indiana.edu/academics/grad-programs/index.html",
        "contact_url": "https://luddy.iu.edu/about/contact.html",
    },
    {
        "id": "kelley",
        "full_name": "Kelley School of Business",
        "keywords": [
            "Kelley", "Business", "MBA", "MSIS",
            "Finance", "Accounting", "Marketing",
            "Supply Chain", "Management",
        ],
        "program_url": "https://kelley.iu.edu/programs/index.html",
        "contact_url": "https://kelley.iu.edu/about/contact.html",
    },
    {
        "id": "arts_sciences",
        "full_name": "College of Arts and Sciences",
        "keywords": [
            "Arts and Sciences", "Arts & Sciences", "College",
            "Liberal Arts", "Biology", "Chemistry", "Physics",
            "Mathematics", "English", "History", "Psychology",
            "Political Science", "Economics", "Sociology",
        ],
        "program_url": "https://college.indiana.edu/graduate/index.html",
        "contact_url": "https://college.indiana.edu/contact/index.html",
    },
    {
        "id": "eskenazi",
        "full_name": "Eskenazi School of Art, Architecture + Design",
        "keywords": [
            "Eskenazi", "Architecture", "Art", "Design",
            "Fine Arts", "Graphic Design", "Studio Art",
        ],
        "program_url": "https://eskenazi.indiana.edu/graduate/index.html",
        "contact_url": "https://eskenazi.indiana.edu/undergraduate/visit.html",
    },
    {
        "id": "jacobs",
        "full_name": "Jacobs School of Music",
        "keywords": [
            "Jacobs", "Music", "Music School",
            "Performance", "Composition", "Music Education",
        ],
        "program_url": "https://music.indiana.edu/admissions/how-to-apply/graduate.html",
        "contact_url": "https://music.indiana.edu/contact/index.html",
    },
    {
        "id": "maurer",
        "full_name": "Maurer School of Law",
        "keywords": [
            "Maurer", "Law", "Law School",
            "JD", "LLM", "SJD", "Legal",
        ],
        "program_url": "https://law.indiana.edu/academics/graduate-degrees/overview/index.html",
        "contact_url": "https://law.indiana.edu/about/contact-us.html",
    },
    {
        "id": "oneill",
        "full_name": "O'Neill School of Public and Environmental Affairs",
        "keywords": [
            "O'Neill", "ONeill", "Oneill", "Public Affairs",
            "Public Policy", "Environmental", "MPA",
            "Nonprofit", "Policy",
        ],
        "program_url": "https://oneill.indiana.edu/masters/degrees-certificates/index.html",
        "contact_url": "https://oneill.indiana.edu/contact/index.html",
    },
    {
        "id": "education",
        "full_name": "School of Education",
        "keywords": [
            "Education", "Teaching", "Teacher",
            "Curriculum", "Educational Leadership",
            "Higher Education", "Instructional",
        ],
        "program_url": "https://education.indiana.edu/programs/graduate/masters/index.html",
        "contact_url": "https://education.indiana.edu/about/contact/index.html",
    },
    {
        "id": "medicine",
        "full_name": "School of Medicine",
        "keywords": [
            "Medicine", "Medical", "Medical School",
            "MD", "Biomedical", "Anatomy",
        ],
        "program_url": "https://medicine.iu.edu/graduate-degrees",
        "contact_url": "https://medicine.iu.edu/bloomington/leadership",
    },
    {
        "id": "nursing",
        "full_name": "School of Nursing",
        "keywords": [
            "Nursing", "Nurse", "BSN", "MSN",
            "DNP", "Nurse Practitioner",
        ],
        "program_url": "https://nursing.iu.edu/bloomington/admissions/graduate/index.html",
        "contact_url": "https://nursing.iu.edu/bloomington/about/contact-us/index.html",
    },
    {
        "id": "optometry",
        "full_name": "School of Optometry",
        "keywords": [
            "Optometry", "Vision", "Vision Science",
            "OD", "Eye", "Optometrist",
        ],
        "program_url": "https://optometry.iu.edu/admissions-academics/vision-science-ms-phd/index.html",
        "contact_url": "https://optometry.iu.edu/admissions-academics/vision-science-ms-phd/index.html",
    },
    {
        "id": "public_health",
        "full_name": "School of Public Health",
        "keywords": [
            "Public Health", "Epidemiology", "MPH",
            "Biostatistics", "Health Policy",
            "Environmental Health", "Global Health",
        ],
        "program_url": "https://publichealth.indiana.edu/masters/degrees-majors/index.html",
        "contact_url": "https://publichealth.indiana.edu/about/contact.html",
    },
    {
        "id": "social_work",
        "full_name": "School of Social Work",
        "keywords": [
            "Social Work", "MSW", "Social Worker",
            "Community Practice", "Clinical Social Work",
        ],
        "program_url": "https://socialwork.iu.edu/index.html",
        "contact_url": "https://socialwork.iu.edu/contact-us/",
    },
    {
        "id": "media",
        "full_name": "The Media School",
        "keywords": [
            "Media School", "Media", "Journalism",
            "Communication", "Film", "Telecommunications",
        ],
        "program_url": "https://mediaschool.indiana.edu/academics/graduate/index.html",
        "contact_url": "https://mediaschool.indiana.edu/about/contact/index.html",
    },
]
