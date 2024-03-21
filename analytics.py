from sqlalchemy.orm import Session
from models import Analytics, ShortenedURL

def update_analytics(db: Session, short_url: str, referrer: str = None):
    shortened_url = db.query(ShortenedURL).filter(ShortenedURL.short_url == short_url).first()
    if shortened_url:
        analytics_entry = db.query(Analytics).filter(Analytics.shortened_url_id == shortened_url.id).first()
        if analytics_entry:
            analytics_entry.total_clicks += 1
            if referrer:
                referrer_sources = analytics_entry.referral_sources.split(",") if analytics_entry.referral_sources else []
                if referrer not in referrer_sources:
                    referrer_sources.append(referrer)
                    analytics_entry.referral_sources = ",".join(referrer_sources)
        else:
            new_analytics = Analytics(shortened_url=shortened_url)
            db.add(new_analytics)
        db.commit()

def get_analytics(db: Session, short_url: str):
    shortened_url = db.query(ShortenedURL).filter(ShortenedURL.short_url == short_url).first()
    if shortened_url:
        analytics_entry = db.query(Analytics).filter(Analytics.shortened_url_id == shortened_url.id).first()
        if analytics_entry:
            return {
                "total_clicks": analytics_entry.total_clicks,
                "referral_sources": analytics_entry.referral_sources.split(",") if analytics_entry.referral_sources else [],
                "created_at": analytics_entry.created_at
            }
    return None