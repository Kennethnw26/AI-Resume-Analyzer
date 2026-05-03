import re
import spacy

nlp = spacy.load("en_core_web_sm")

# Comprehensive skill vocabulary with canonical names and aliases
SKILL_VOCAB = {
    # Programming Languages
    "python": ["python", "python3", "python2"],
    "java": ["java", "java ee", "java se"],
    "javascript": ["javascript", "js", "es6", "es2015", "ecmascript"],
    "typescript": ["typescript", "ts"],
    "c++": ["c++", "cpp", "c plus plus"],
    "c#": ["c#", "csharp", "c sharp", ".net c#"],
    "c": ["c language", " c "],
    "r": [" r ", "r programming", "r language"],
    "go": ["golang", " go "],
    "rust": ["rust", "rust lang"],
    "kotlin": ["kotlin"],
    "swift": ["swift"],
    "scala": ["scala"],
    "ruby": ["ruby", "ruby on rails"],
    "php": ["php"],
    "perl": ["perl"],
    "matlab": ["matlab"],
    "bash": ["bash", "shell scripting", "shell script", "bash scripting"],
    "powershell": ["powershell"],

    # Web Frameworks & Libraries
    "react": ["react", "react.js", "reactjs"],
    "angular": ["angular", "angularjs", "angular.js"],
    "vue": ["vue", "vue.js", "vuejs"],
    "node.js": ["node.js", "nodejs", "node js", "express.js", "expressjs"],
    "django": ["django"],
    "flask": ["flask"],
    "fastapi": ["fastapi", "fast api"],
    "spring": ["spring", "spring boot", "spring framework"],
    "asp.net": ["asp.net", "aspnet", "asp net"],
    "laravel": ["laravel"],
    "next.js": ["next.js", "nextjs", "next js"],
    "svelte": ["svelte"],
    "tailwind": ["tailwind", "tailwindcss", "tailwind css"],
    "bootstrap": ["bootstrap"],
    "jquery": ["jquery"],
    "graphql": ["graphql"],
    "rest api": ["rest api", "restful", "rest", "restful api"],

    # Data Science & ML
    "machine learning": ["machine learning", "ml"],
    "deep learning": ["deep learning", "dl"],
    "nlp": ["nlp", "natural language processing"],
    "computer vision": ["computer vision", "cv"],
    "data analysis": ["data analysis", "data analytics", "data analyst"],
    "data visualization": ["data visualization", "data viz"],
    "statistical analysis": ["statistical analysis", "statistics", "statistical modeling"],
    "tensorflow": ["tensorflow", "tf"],
    "pytorch": ["pytorch", "torch"],
    "keras": ["keras"],
    "scikit-learn": ["scikit-learn", "sklearn", "scikit learn"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "matplotlib": ["matplotlib"],
    "seaborn": ["seaborn"],
    "scipy": ["scipy"],
    "xgboost": ["xgboost", "xgb"],
    "lightgbm": ["lightgbm", "lgbm"],
    "hugging face": ["hugging face", "huggingface", "transformers"],
    "llm": ["llm", "large language model", "llms"],
    "rag": ["rag", "retrieval augmented generation"],

    # Databases
    "sql": ["sql", "structured query language"],
    "mysql": ["mysql"],
    "postgresql": ["postgresql", "postgres"],
    "sqlite": ["sqlite"],
    "mongodb": ["mongodb", "mongo"],
    "redis": ["redis"],
    "cassandra": ["cassandra"],
    "elasticsearch": ["elasticsearch", "elastic search"],
    "dynamodb": ["dynamodb", "dynamo db"],
    "firebase": ["firebase"],
    "neo4j": ["neo4j"],
    "oracle": ["oracle db", "oracle database"],
    "ms sql server": ["ms sql", "sql server", "microsoft sql server", "mssql"],

    # Cloud & DevOps
    "aws": ["aws", "amazon web services"],
    "azure": ["azure", "microsoft azure"],
    "gcp": ["gcp", "google cloud", "google cloud platform"],
    "docker": ["docker"],
    "kubernetes": ["kubernetes", "k8s"],
    "terraform": ["terraform"],
    "ansible": ["ansible"],
    "ci/cd": ["ci/cd", "ci cd", "continuous integration", "continuous deployment", "continuous delivery"],
    "jenkins": ["jenkins"],
    "github actions": ["github actions"],
    "gitlab ci": ["gitlab ci", "gitlab"],
    "linux": ["linux", "unix"],
    "nginx": ["nginx"],

    # Tools & Platforms
    "git": ["git", "github", "gitlab", "bitbucket", "version control"],
    "jira": ["jira", "confluence", "atlassian"],
    "agile": ["agile", "scrum", "kanban", "sprint"],
    "excel": ["excel", "microsoft excel", "ms excel"],
    "power bi": ["power bi", "powerbi"],
    "tableau": ["tableau"],
    "looker": ["looker", "looker studio"],
    "airflow": ["airflow", "apache airflow"],
    "spark": ["apache spark", "pyspark", "spark"],
    "kafka": ["kafka", "apache kafka"],
    "hadoop": ["hadoop", "hdfs", "mapreduce"],
    "dbt": ["dbt", "data build tool"],

    # Security
    "cybersecurity": ["cybersecurity", "cyber security", "information security", "infosec"],
    "penetration testing": ["penetration testing", "pentesting", "pen testing"],
    "network security": ["network security"],

    # General & Soft Skills
    "problem solving": ["problem solving", "problem-solving", "analytical thinking"],
    "communication": ["communication", "written communication", "verbal communication"],
    "leadership": ["leadership", "team lead", "team leadership"],
    "project management": ["project management", "pmp"],
    "teamwork": ["teamwork", "collaboration", "cross-functional"],
    "time management": ["time management"],
    "critical thinking": ["critical thinking"],
}

# Build a flat lookup: alias -> canonical name
_ALIAS_MAP: dict[str, str] = {}
for canonical, aliases in SKILL_VOCAB.items():
    for alias in aliases:
        _ALIAS_MAP[alias.lower()] = canonical

# Sort aliases longest-first so longer phrases match before substrings
_SORTED_ALIASES = sorted(_ALIAS_MAP.keys(), key=len, reverse=True)


def extract_skills(text: str) -> list[str]:
    """Extract canonical skill names from text using phrase matching with word boundaries."""
    if not text or not text.strip():
        return []

    lower = text.lower()
    found = set()

    for alias in _SORTED_ALIASES:
        # Use word boundaries to avoid false positives like "c" matching "access"
        pattern = r"(?<![a-zA-Z0-9+#])" + re.escape(alias) + r"(?![a-zA-Z0-9+#])"
        if re.search(pattern, lower):
            found.add(_ALIAS_MAP[alias])

    return sorted(found)
