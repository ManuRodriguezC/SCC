def calculateInterScore(request):
    score = 750
    moreYear = request.POST.get('moreYears')
    if moreYear == "Hasta 30":
        score -= 20
    elif moreYear == "Mayor a 30 Menor a 50":
        score -= 15
    else:
        score += 30
    moreState = request.POST.get('moreState')
    if moreState == "Soltero" or moreState == "Union Libre":
        score -= 10
    moreLive = request.POST.get('moreLive')
    if moreLive == "Familiar / Arriendo":
        score -= 25
    else:
        score += 25
    moreStudy = request.POST.get('moreStudy')
    if moreStudy == "Desconocido":
        score -= 10
    else:
        score -= 15
    moreIng = request.POST.get('moreIng')
    if moreIng == "Hasta 2 SMMLV":
        score -= 10
    else:
        score += 20
    moreGender = request.POST.get('moreGender')
    if moreGender == "Masculino" and moreYear == "Hasta 30":
        score -= 15
    if moreGender == "Masculino" and moreState == "Soltero":
        score -= 15
    if (moreState == "Casado" or moreState == "Union Libre") and moreLive == "Familiar / Arriendo":
        score -= 5
    moreTime = request.POST.get('moreTime')
    if moreLive == "Familiar / Arriendo" and moreTime == "Hasta 4 años":
        score -= 10
    if score >= 800:
        score += 30 
    return score