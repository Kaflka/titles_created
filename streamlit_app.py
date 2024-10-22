import streamlit as st
from generate_xiaohongshu import generate_xiaohongshu

def main():
    st.title("小红书标题生成器✏️")
    st.write("快输入一个主题试试吧！")

    st.header("星火API配置")
    spark_app_id = st.text_input("请输入 SPARKAI_APP_ID", type="password")
    spark_api_secret = st.text_input("请输入 SPARKAI_API_SECRET", type="password")
    spark_api_key = st.text_input("请输入 SPARKAI_API_KEY", type="password")

    st.header("生成标题")
    theme = st.text_input("主题", "")

    if st.button("生成标题"):
        if theme and spark_app_id and spark_api_secret and spark_api_key:
            with st.spinner("正在生成标题..."):
                try:
                    titles = generate_xiaohongshu(theme, spark_app_id, spark_api_secret, spark_api_key)
                    if titles:
                        st.success("生成的标题列表：")
                        for i, title in enumerate(titles, 1):
                            st.write(f"{i}. {title}")
                    else:
                        st.error("生成标题失败，请检查输入和模型响应。")
                except Exception as e:
                    st.error(f"生成标题时发生错误: {e}")
        else:
            st.warning("请填写所有API配置和主题。")

if __name__ == '__main__':
    main()
