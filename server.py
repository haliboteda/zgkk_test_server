from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json

app = FastAPI()

response_json_TZ = {
    "success": True,
    "customer_name": "温州市管阁通信息技术有限公司",
    "order_no": "",
    "Data": [
        {
            "order_no": "BK2109N0001",
            "customer_name": "温州市管阀通信息技术有限公司",
            "line": 1,
            "item_no": "0100100691",
            "item_name": "八角热",
            "material": "316L",
            "DN": "R57(392,11*369,89x15,88x7,75)",
            "set_pressure": "0.73",
            "quantity": 200,
            "remark": "",
            "valve_seqs": "GFT240400001-GFT240400200",
            "material_inner": "316L"
        },
        {
            "order_no": "BK2109N0001",
            "customer_name": "温州市管阀通信息技术有限公司",
            "line": 2,
            "item_no": "100180692",
            "item_name": "八角垫",
            "material": "316L",
            "DN": "R45(222,23*200,01*15,88*7,75)",
            "set_pressure": "1.5",
            "quantity": 300,
            "remark": "",
            "valve_seqs": "GFT250400104-GFT250400403",
            "material_inner": ""
        },
        {
            "order_no": "BK2109N0001",
            "customer_name": "温州市管阁通信息技术有限公司",
            "line": 3,
            "item_no": "0100160693",
            "item_name": "八角垫",
            "material": "316L",
            "DN": "R53(334,96*312,76*16,88*7,75)",
            "set_pressure": "2.0",
            "quantity": 400,
            "remark": "",
            "valve_seqs": "GFT251100101-GFT251100500",
            "material_inner": ""
        }
    ]
}

response_json_BY = {
    "success": True,
    "customer_name": "客户名称",
    "work_no": "作业指令号", 
    "assembly_no":"装配单号",
    "details": [
        {
            "item_no":"1",# 序号
            "item_name": "产品名称1", 
            "item_model": "A41Y-25P 1E2",
            "material": "WCB", 
            "DN": "DN250", # 公称通径，如果是DN请以DN开头，如果是NPS，请以NPS开头
            "PN": "PN250",# 公称压力，如果是PN请以PN开头，如果是CL，请以CL开头
            "PS":"1.96",#整定压力MPa
            "housing":"bb",#壳体强度
            "quantity": "3", # 阀门数量
            "item_code": "51940001-003",# 该序号下第一个阀门编号（测量过程过程中，系统会根据第一个阀门编号和阀门数量自动顺延出后面的编号）,
        },
        {
            "item_no":"2",# 序号
            "item_name": "产品名称2", 
            "item_model": "A41Y-25P 1E2",
            "material": "WCB", 
            "DN": "NPS250", # 公称通径，如果是DN请以DN开头，如果是NPS，请以NPS开头
            "PN": "CL250",# 公称压力，如果是PN请以PN开头，如果是CL，请以CL开头
            "PS":"1.962",#整定压力MPa
            "housing":"aa",#壳体强度
            "quantity": "10", # 阀门数量
            "item_code": "2603201-210",# 该序号下第一个阀门编号（测量过程过程中，系统会根据第一个阀门编号和阀门数量自动顺延出后面的编号）,
        }
    ]
}

@app.post("/test/TZ")
async def test_tz(request: Request):

    body = await request.json()

    num = body.get("num", "")

    if "TZ2410N0199" in num:
        return JSONResponse(content=response_json_TZ)

    return JSONResponse(content=None)

@app.post("/test/test")
async def test_test(request: Request):
    response_json = {
        "code": "hello world"
    }
    return JSONResponse(content=response_json)


# 


@app.post("/test/by")
async def test_BY(request: Request):

    body = await request.json()

    num = body.get("order_code", "")

    if "25152" in num:
        return JSONResponse(content=response_json_BY)

    return JSONResponse(content=None)