from turtle import *


def snowflake(size,level):
    if level == 0:
        forward(size)
        return

    size /= 3
    snowflake(size,level-1)
    left(60)
    snowflake(size, level - 1)
    right(120)
    snowflake(size, level - 1)
    left(60)
    snowflake(size, level - 1)


penup()
goto(-690,-300)
pendown()
speed(0)
snowflake(1380,5)
done()