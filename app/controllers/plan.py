from flask import current_app, request

from app.models.plan import Plans, db

def create_plan():
    data = request.get_json()  # 从请求体里解析 JSON
    userid = data.get("userid")
    plan_date = data.get("selectedDate")
    title = data.get("title")
    start = data.get("start")
    end = data.get("end")

    if not userid or not userid:
        return {'code': 400, 'msg': '请重新登录'}
    if not plan_date or not plan_date:
        return {'code': 400, 'msg': '日期不能为空'}
    if not title or not title:
        return {'code': 400, 'msg': '内容不能为空'}
    if not start or not start:
        return {'code': 400, 'msg': '开始时间不能为空'}
    if not end or not end:
        return {'code': 400, 'msg': '结束时间不能为空'}
    
    plan = Plans(userid=userid, plan_date=plan_date, title=title, start_time=start, end_time=end)

    with current_app.app_context():
        db.session.add(plan)
        db.session.commit()

    return {'code': 200, 'msg': 'success'}