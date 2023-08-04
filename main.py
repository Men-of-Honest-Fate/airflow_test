import requests as r
from airflow.decorators import dag, task
from datetime import datetime, timedelta


@task(task_id='Test airflow in docker', retries=3)
def test(chat_id):
    response = r.get('https://www.google.com').text

    r.post(
        f'https://api.telegram.org/bot{6191282882:AAE1CwZn4GbGyO4ttL7fesNrn9I4lDa7w2k}/sendMessage',
        json={
            "chat_id": chat_id,
            "text": response,
        }
    )


@dag(
    schedule='0 */12 * * *',
    start_date=datetime(2023, 1, 1, 2, 0, 0),
    catchup=False,
    tags=["infra"],
    default_args={
        "owner": "infra",
        "retries": 3,
        "retry_delay": timedelta(minutes=5)
    }
)
def check_vds_balance():
    balance = test(818677727)


check_vds_balance()
