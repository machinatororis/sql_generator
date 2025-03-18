from llm import generate_sql


def main():
    print("🔹 SQL Generator на основе LLM")
    print("Введите ваш запрос (например: 'Выбери всех пользователей с Gmail'):")

    user_input = input(">> ")
    sql_query = generate_sql(user_input)

    print("\n💡 Сгенерированный SQL-запрос:\n")
    print(sql_query)


if __name__ == "__main__":
    main()
