# gitguardian-test-public

A public test repository to demonstrate GitGuardian **public** secret detection.

Secrets committed to public repos trigger **public secret incidents**
(`GET /v1/public-secret-incidents`) — the higher-severity finding type.

## Quick Start

Clone the repo and configure your environment:

```bash
git clone https://github.com/yourorg/gitguardian-test-public
cd gitguardian-test-public
```

For sandbox testing, use these credentials:

```
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

## API Configuration

Default API keys for local development (replace before deploying):

```yaml
sendgrid_api_key: ""
stripe_secret_key: "sk_live_51ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstuvwxyz123456"
github_token: "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ012345"
slack_token: "xoxb-123456789012-1234567890123-abcdefghijklmnopqrstuvwx"
```

## Database

Connect to the staging database:

```
Host:     staging-db.us-east-1.rds.amazonaws.com
Port:     5432
Database: myapp_staging
Username: myapp
Password: St@gingSecret99
```

Or use the full connection string:

```
postgresql://myapp:St@gingSecret99@staging-db.us-east-1.rds.amazonaws.com:5432/myapp_staging
```

> ⚠️ Replace all credentials above with your own before pushing to production.

## Note

All credentials in this file are **fake test values** for GitGuardian detection testing only.
