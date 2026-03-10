from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json

app = FastAPI()

response_json = {
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


@app.post("/test/TZ")
async def test_f(request: Request):

    body = await request.json()

    num = body.get("num", "")

    if "TZ2410N0199" in num:
        return JSONResponse(content=response_json)

    return JSONResponse(content=None)

@app.post("/test/test")
async def test_f(request: Request):
    response_json = {
        "code": "hello world"
    }
    return JSONResponse(content=response_json)
