import random

# Danh sách các lá bài Tarot và ý nghĩa của chúng
tarot_deck = {
    1: ("The Fool", "Khởi đầu mới, tiềm năng, tự do"),
    2: ("The Magician", "Sáng tạo, hành động, quyền lực"),
    3: ("The High Priestess", "Trực giác, bí ẩn, tri thức"),
    4: ("The Empress", "Tình yêu, sự sáng tạo, thiên nhiên"),
    5: ("The Emperor", "Quyền lực, ổn định, lãnh đạo"),
    6: ("The Hierophant", "Truyền thống, tôn giáo, giáo dục"),
    7: ("The Lovers", "Tình yêu, sự lựa chọn, hài hòa"),
    8: ("The Chariot", "Quyết tâm, kiểm soát, chiến thắng"),
    9: ("Strength", "Sức mạnh, dũng cảm, kiên nhẫn"),
    10: ("The Hermit", "Sự tĩnh lặng, tìm kiếm tri thức, cô đơn"),
    11: ("Wheel of Fortune", "Số phận, sự thay đổi, cơ hội"),
    12: ("Justice", "Công lý, sự thật, trách nhiệm"),
    13: ("The Hanged Man", "Hy sinh, nhìn nhận từ góc độ khác, giải thoát"),
    14: ("Death", "Sự kết thúc, sự biến đổi, sự khởi đầu mới"),
    15: ("Temperance", "Cân bằng, điều độ, hòa hợp"),
    16: ("The Devil", "Ràng buộc, cám dỗ, hạn chế"),
    17: ("The Tower", "Sự đổ vỡ, thay đổi bất ngờ, sự thức tỉnh"),
    18: ("The Star", "Hy vọng, niềm tin, sự chữa lành"),
    19: ("The Moon", "Ảo tưởng, trực giác, giấc mơ"),
    20: ("The Sun", "Thành công, hạnh phúc, tích cực"),
    21: ("Judgement", "Phán xét, sự tái sinh, sự suy ngẫm"),
    22: ("The World", "Hoàn thành, thành tựu, kết thúc"),
    23: ("Ace of Cups", "Tình yêu, lòng trắc ẩn, sự khởi đầu tình cảm mới"),
    24: ("Two of Cups", "Quan hệ đối tác, sự hài hòa, sự kết nối"),
    25: ("Three of Cups", "Lễ hội, tình bạn, cộng đồng"),
    26: ("Four of Cups", "Suy ngẫm, không hài lòng, cơ hội bỏ lỡ"),
    27: ("Five of Cups", "Hối tiếc, thất vọng, mất mát"),
    28: ("Six of Cups", "Nỗi nhớ, hồi ức, sự vô tư"),
    29: ("Seven of Cups", "Ảo tưởng, sự lựa chọn, mơ mộng"),
    30: ("Eight of Cups", "Từ bỏ, tìm kiếm sự thật, đi tìm điều mới"),
    31: ("Nine of Cups", "Sự hài lòng, thỏa mãn, ước muốn"),
    32: ("Ten of Cups", "Hạnh phúc gia đình, sự viên mãn, mối quan hệ bền vững"),
    33: ("Page of Cups", "Lời nhắn tình cảm, sự nhạy cảm, khởi đầu sáng tạo"),
    34: ("Knight of Cups", "Sự quyến rũ, lý tưởng lãng mạn, theo đuổi ước mơ"),
    35: ("Queen of Cups", "Lòng từ bi, sự chăm sóc, trí tưởng tượng"),
    36: ("King of Cups", "Sự cân bằng cảm xúc, lòng trắc ẩn, kiểm soát tình cảm"),
    37: ("Ace of Pentacles", "Khởi đầu mới về tài chính, cơ hội, thịnh vượng"),
    38: ("Two of Pentacles", "Cân bằng, linh hoạt, thích nghi"),
    39: ("Three of Pentacles", "Làm việc nhóm, sự công nhận, kỹ năng"),
    40: ("Four of Pentacles", "Kiểm soát, ổn định tài chính, bảo vệ"),
    41: ("Five of Pentacles", "Khó khăn tài chính, mất mát, cảm giác bị bỏ rơi"),
    42: ("Six of Pentacles", "Cho và nhận, lòng từ thiện, sự hào phóng"),
    43: ("Seven of Pentacles", "Kiên nhẫn, đánh giá, chờ đợi kết quả"),
    44: ("Eight of Pentacles", "Làm việc chăm chỉ, kỹ năng, sự tận tụy"),
    45: ("Nine of Pentacles", "Sự độc lập, thành tựu, sự tự hào"),
    46: ("Ten of Pentacles", "Di sản, truyền thống gia đình, sự ổn định tài chính"),
    47: ("Page of Pentacles", "Học hỏi, cơ hội mới, tò mò"),
    48: ("Knight of Pentacles", "Sự tận tâm, trách nhiệm, kiên trì"),
    49: ("Queen of Pentacles", "Chăm sóc, sự hào phóng, sự thoải mái"),
    50: ("King of Pentacles", "Thành công tài chính, lãnh đạo, sự thịnh vượng"),
    51: ("Ace of Swords", "Sự rõ ràng, ý tưởng mới, sự thật"),
    52: ("Two of Swords", "Sự bế tắc, sự lựa chọn khó khăn, không chắc chắn"),
    53: ("Three of Swords", "Đau khổ, tổn thương, mất mát"),
    54: ("Four of Swords", "Nghỉ ngơi, hồi phục, suy ngẫm"),
    55: ("Five of Swords", "Xung đột, mất mát, căng thẳng"),
    56: ("Six of Swords", "Chuyển đổi, vượt qua khó khăn, hành trình"),
    57: ("Seven of Swords", "Lừa dối, kế hoạch bí mật, sự rời bỏ"),
    58: ("Eight of Swords", "Cảm giác bị mắc kẹt, hạn chế, sợ hãi"),
    59: ("Nine of Swords", "Lo lắng, căng thẳng, ác mộng"),
    60: ("Ten of Swords", "Kết thúc, sự phản bội, khủng hoảng"),
    61: ("Page of Swords", "Tò mò, sự giám sát, ý tưởng mới"),
    62: ("Knight of Swords", "Hành động nhanh chóng, tham vọng, sự năng động"),
    63: ("Queen of Swords", "Sự rõ ràng, trí tuệ, sự độc lập"),
    64: ("King of Swords", "Sự lãnh đạo, sự thật, quyết đoán"),
    65: ("Ace of Wands", "Cảm hứng, sự sáng tạo, cơ hội mới"),
    66: ("Two of Wands", "Kế hoạch, sự quyết định, khám phá"),
    67: ("Three of Wands", "Mở rộng, sự lãnh đạo, tầm nhìn"),
    68: ("Four of Wands", "Lễ kỷ niệm, sự hài lòng, đoàn kết"),
    69: ("Five of Wands", "Xung đột, sự cạnh tranh, căng thẳng"),
    70: ("Six of Wands", "Chiến thắng, công nhận, thành công"),
    71: ("Seven of Wands", "Bảo vệ, kiên định, thách thức"),
    72: ("Eight of Wands", "Hành động nhanh, tiến bộ, thông tin"),
    73: ("Nine of Wands", "Kiên trì, sự phòng thủ, bền bỉ"),
    74: ("Ten of Wands", "Gánh nặng, trách nhiệm, sự mệt mỏi"),
    75: ("Page of Wands", "Sự khám phá, nhiệt huyết, khởi đầu sáng tạo"),
    76: ("Knight of Wands", "Sự phiêu lưu, sự tự tin, năng lượng"),
    77: ("Queen of Wands", "Sự quyến rũ, sáng tạo, sự tự tin"),
    78: ("King of Wands", "Lãnh đạo, tầm nhìn, quyền lực"),
}

# Tạo 3 số ngẫu nhiên từ 1 đến 78
random_cards = random.sample(range(1, 79), 3)

# Tra cứu các lá bài Tarot tương ứng và ý nghĩa của chúng
drawn_cards = [tarot_deck[card] for card in random_cards]

# Đưa ra giải bài tổng thể
def interpret_tarot(cards):
    interpretation = "Giải bài Tarot của bạn:\n"
    for i, card in enumerate(cards, start=1):
        interpretation += f"Lá bài {i}: {card[0]} - {card[1]}\n"
    interpretation += "\nTổng thể: "
    interpretation += "Các lá bài này cho thấy một quá trình biến đổi và phát triển quan trọng. " \
                      "Bạn đang đứng trước những khởi đầu mới, cần tìm kiếm sự cân bằng và chuẩn bị " \
                      "cho những thay đổi bất ngờ. Hãy tin vào trực giác và sức mạnh bên trong bạn, " \
                      "và đón nhận mọi thách thức với tinh thần lạc quan."
    return interpretation

# Hiển thị kết quả
result = interpret_tarot(drawn_cards)
print(result)
