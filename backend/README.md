
## activate virtual environment
source .venv/bin/activate

## install the required software version
pip install -r requirements.txt

## running backend
python app.py


Week 1 — Foundation
    Project setup (repo, env, linting, formatting)
    Database schema v1 (User, Account, Category, Transaction)
    Auth (register/login/logout) working
    Basic API skeleton + health check endpoint
Week 2 — Core money engine
    Transactions CRUD (create/edit/delete/list)
    Account balances computed correctly (no floats — cents only)
    Seed default categories
    Basic unit tests for balance + transfers (even if transfers come later)
Week 3 — UI baseline
    Simple frontend pages (or React screens) to:
    Add transaction
    View transaction list
    View accounts + balances
    Input validation + error messages
Week 4 — Reporting
    Monthly summary
    Category breakdown chart
    Filters (date range, account, category)
Week 5 — “Looks professional” features
    CSV export (or import)
    Recurring transactions (simple version)
    Polishing: loading states, empty states, better UI
Week 6 — Deployment + CV packaging
    Deploy (Render/Railway/Fly or AWS)
    README with screenshots + architecture diagram
Test coverage pass
    Short demo video (optional but powerful)