def calculate_landed_cost(car, fx):
    hammer_gbp = car["hammer_jpy"] * fx

    jp_fees = 500
    inland = 150
    freight = 1000

    duty_base = hammer_gbp + jp_fees + inland + freight
    duty = duty_base * 0.10
    vat = (duty_base + duty) * 0.20

    uk_fees = 300
    mph_conversion = 400

    total = hammer_gbp + jp_fees + inland + freight + duty + vat + uk_fees + mph_conversion

    return {
        "hammer_gbp": round(hammer_gbp, 2),
        "landed_gbp": round(total, 2)
    }
