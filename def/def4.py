import math
SQUARE=10
PAINT_FOR_SQUARE=5
TIME_FOR_SQUARE=8
PAY_HOUR=2000
def main():
    square_example=float(input("Enter square: \n"))
    price_of_paint=float(input("Enter price of paint: \n"))
    paintCount_5_kg, hours_count, cost_paint, cost_work, total_cost=calculate(square_example,price_of_paint)
    print(f"Понадобиться: {paintCount_5_kg} банки(ок) краски\n Затратиться {hours_count} часов работы\n Стоимость краски составит: ${cost_paint:,.2f} \n"
          f"Cтоимость работы составит ${cost_work:,.2f} \n"
          f"Общая стоимость составит ${total_cost:,.2f}")
def calculate (squareFact,pricePaint):
    ratio=squareFact/SQUARE
    paintCount_5_kg=math.ceil(ratio)
    hoursCount=int(TIME_FOR_SQUARE*ratio)
    costPaint=paintCount_5_kg*pricePaint
    costWork=PAY_HOUR*hoursCount
    totalCost=costWork+costPaint
    return(paintCount_5_kg,hoursCount,costPaint,costWork,totalCost)
main()