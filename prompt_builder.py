from trends import get_trend

def build_prompt(user_prompt):
    trend = get_trend()

    return f"""
    professional fashion photography,
    {trend},
    {user_prompt},
    magazine quality,
    realistic lighting,
    commercial photo shoot
    """
