CATEGORY_DEFAULTS = {
    "sneakers": {
        "iva": 0.22,
        "channel_margin": 0.28,
        "distribution": 0.10,
        "marketing": 0.12,
        "brand_premium": 0.08,
        "commercial_overhead": 0.05,
    },
    "electronics": {
        "iva": 0.22,
        "channel_margin": 0.14,
        "distribution": 0.07,
        "marketing": 0.08,
        "brand_premium": 0.06,
        "commercial_overhead": 0.04,
    },
    "cosmetics": {
        "iva": 0.22,
        "channel_margin": 0.32,
        "distribution": 0.12,
        "marketing": 0.18,
        "brand_premium": 0.12,
        "commercial_overhead": 0.06,
    },
    "furniture": {
        "iva": 0.22,
        "channel_margin": 0.24,
        "distribution": 0.10,
        "marketing": 0.05,
        "brand_premium": 0.04,
        "commercial_overhead": 0.05,
    },
    "apparel": {
        "iva": 0.22,
        "channel_margin": 0.30,
        "distribution": 0.10,
        "marketing": 0.14,
        "brand_premium": 0.10,
        "commercial_overhead": 0.05,
    },
}

BRAND_ADJUSTMENTS = {
    "low": {"brand_premium": -0.04, "marketing": -0.03},
    "medium": {"brand_premium": 0.00, "marketing": 0.00},
    "premium": {"brand_premium": 0.06, "marketing": 0.03},
}

CHANNEL_ADJUSTMENTS = {
    "direct": {"channel_margin": -0.10, "distribution": -0.03},
    "retail": {"channel_margin": 0.00, "distribution": 0.00},
}

def estimate_cost(product, price, category, brand, channel):
    params = CATEGORY_DEFAULTS[category].copy()

    for k, v in BRAND_ADJUSTMENTS[brand].items():
        params[k] += v

    for k, v in CHANNEL_ADJUSTMENTS[channel].items():
        params[k] += v

    iva = params["iva"]
    price_net = price / (1 + iva)

    non_productive = (
        params["channel_margin"]
        + params["distribution"]
        + params["marketing"]
        + params["brand_premium"]
        + params["commercial_overhead"]
    )

    real_cost = price_net * (1 - non_productive)

    return {
        "product": product,
        "price_final": round(price, 2),
        "price_net": round(price_net, 2),
        "real_cost": round(real_cost, 2),
        "non_productive_share": round(non_productive, 2)
    }
