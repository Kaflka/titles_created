from prompt_template import system_template_text
from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage
import re

SPARKAI_URL = 'wss://spark-api.xf-yun.com/v3.5/chat'
SPARKAI_DOMAIN = 'generalv3.5'

def generate_xiaohongshu(theme, spark_app_id, spark_api_secret, spark_api_key):
    spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=spark_app_id,
        spark_api_key=spark_api_key,
        spark_api_secret=spark_api_secret,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=False,
    )
    messages = [
        ChatMessage(role="system", content=system_template_text),
        ChatMessage(role="user", content=theme),
    ]
    handler = ChunkPrintHandler()
    response = spark.generate([messages], callbacks=[handler])

    try:
        generated_text = response.generations[0][0].text.strip()

        titles = re.findall(r'^\d+\.?\s*(.*)$', generated_text, re.MULTILINE)

        if not titles:
            titles = generated_text.split('\n')

        titles = [title.strip() for title in titles if title.strip()]

        if len(titles) != 5:
            raise ValueError("生成的标题数量不足5个。")

        return titles

    except (AttributeError, IndexError, ValueError) as e:
        raise e