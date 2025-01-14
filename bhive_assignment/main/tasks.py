from main.services import BhiveFundService

@app.task(bind=True)
def sync_portfolio_value_hourly(self):
    BhiveFundService().sync_portfolio_value_hourly()
    return
