from poweruserproject.api.business_logic import count_daily_activites_for_a_month, count_users_per_day


def test_count_daily_activities_for_a_month(user_activities):
    expected = {
        '2021-05-01': 2,
        '2021-05-02': 1,
        '2021-05-03': 1,
    }

    assert count_daily_activites_for_a_month(5) == expected


def test_count_users_per_day(user_activities):
    assert 1 == count_users_per_day('2021-05-02')
