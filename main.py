import json
import time
import random
from datetime import datetime
from typing import Dict, List, Optional

class AIShortVideoBGMMatcher:
    """AI短视频背景音乐匹配器"""
    
    def __init__(self):
        # 模拟的音乐库：音乐ID -> (风格, 节奏, 情绪, 时长)
        self.music_library = {
            "M001": ("流行", "快", "欢快", 30),
            "M002": ("电子", "中", "动感", 45),
            "M003": ("古典", "慢", "优雅", 60),
            "M004": ("摇滚", "快", "激情", 40),
            "M005": ("轻音乐", "慢", "放松", 50),
            "M006": ("嘻哈", "快", "酷炫", 35),
            "M007": ("民谣", "中", "温暖", 55),
            "M008": ("爵士", "慢", "浪漫", 65)
        }
        
        # 模拟的用户行为数据
        self.user_behavior_log = []
        
    def analyze_video_content(self, video_description: str) -> Dict:
        """
        分析视频内容（模拟大模型分析）
        实际项目中这里会调用大模型API
        """
        print(f"正在分析视频内容: {video_description}")
        
        # 模拟大模型分析结果
        analysis_result = {
            "dominant_emotion": random.choice(["欢快", "动感", "优雅", "激情", "放松", "温暖"]),
            "content_style": random.choice(["流行", "时尚", "自然", "城市", "艺术", "生活"]),
            "recommended_tempo": random.choice(["快", "中", "慢"]),
            "suitable_duration": random.randint(30, 60)
        }
        
        # 记录分析时间
        analysis_result["analysis_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return analysis_result
    
    def match_bgm(self, video_analysis: Dict) -> List[str]:
        """
        根据视频分析结果匹配背景音乐
        """
        print("正在智能匹配背景音乐...")
        
        matched_music = []
        
        for music_id, (style, tempo, emotion, duration) in self.music_library.items():
            # 简单的匹配逻辑（实际会更复杂）
            match_score = 0
            
            # 情绪匹配
            if video_analysis["dominant_emotion"] in emotion:
                match_score += 3
            elif video_analysis["dominant_emotion"][:2] in emotion:
                match_score += 2
                
            # 节奏匹配
            if video_analysis["recommended_tempo"] == tempo:
                match_score += 2
                
            # 时长匹配（误差在10秒内）
            if abs(duration - video_analysis["suitable_duration"]) <= 10:
                match_score += 1
                
            if match_score >= 3:  # 匹配阈值
                matched_music.append({
                    "music_id": music_id,
                    "style": style,
                    "tempo": tempo,
                    "emotion": emotion,
                    "duration": duration,
                    "match_score": match_score
                })
        
        # 按匹配分数排序
        matched_music.sort(key=lambda x: x["match_score"], reverse=True)
        
        return matched_music[:3]  # 返回前3个推荐
    
    def log_user_behavior(self, user_id: str, action: str, details: Dict):
        """
        记录用户行为数据，用于后续分析优化
        """
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "user_id": user_id,
            "action": action,
            "details": details
        }
        
        self.user_behavior_log.append(log_entry)
        print(f"已记录用户行为: {action}")
        
        # 模拟数据持久化（实际会存到数据库）
        if len(self.user_behavior_log) % 5 == 0:
            self._save_behavior_data()
    
    def _save_behavior_data(self):
        """模拟保存用户行为数据"""
        print(f"已保存 {len(self.user_behavior_log)} 条用户行为记录")
        
    def get_optimization_metrics(self) -> Dict:
        """
        获取功能优化指标（模拟数据分析）
        """
        total_actions = len(self.user_behavior_log)
        bgm_selections = sum(1 for log in self.user_behavior_log 
                           if log["action"] == "select_bgm")
        
        # 模拟停留时长提升数据
        avg_stay_time = 5.0  # 基准停留时间（分钟）
        improvement_rate = 0.18  # 18%提升
        
        return {
            "total_user_actions": total_actions,
            "bgm_selection_count": bgm_selections,
            "avg_stay_time_minutes": avg_stay_time * (1 + improvement_rate),
            "improvement_rate": f"{improvement_rate * 100:.1f}%",
            "feedback_collected": random.randint(200, 250)  # 模拟收集的反馈数量
        }

def main():
    """主函数 - AI短视频配乐匹配系统演示"""
    print("=" * 50)
    print("AI短视频智能配乐匹配系统")
    print("=" * 50)
    
    # 初始化匹配器
    matcher = AIShortVideoBGMMatcher()
    
    # 模拟用户输入视频描述
    video_descriptions = [
        "夏日海滩度假，阳光明媚，海浪拍岸",
        "城市夜景，车流穿梭，霓虹闪烁",
        "温馨家庭聚会，欢声笑语，美食分享",
        "极限运动，滑雪跳跃，速度与激情"
    ]
    
    for i, description in enumerate(video_descriptions[:2], 1):  # 演示前2个
        print(f"\n【场景 {i}】视频描述: {description}")
        
        # 1. 分析视频内容
        video_analysis = matcher.analyze_video_content(description)
        print(f"分析结果: {json.dumps(video_analysis, ensure_ascii=False, indent=2)}")
        
        # 记录用户行为
        matcher.log_user_behavior(
            user_id=f"user_{i:03d}",
            action="analyze_video",
            details={"description": description, "analysis": video_analysis}
        )
        
        # 2. 智能匹配BGM
        recommendations = matcher.match_bgm(video_analysis)
        
        if recommendations:
            print(f"\n为您推荐以下背景音乐:")
            for idx, music in enumerate(recommendations, 1):
                print(f"{idx}. {music['music_id']} - {music['style']}风格 | "
                      f"{music['emotion']}情绪 | {music['duration']}秒 | "
                      f"匹配度:{music['match_score']}/6")
            
            # 模拟用户选择
            selected_music = random.choice(recommendations)
            print(f"\n用户选择了: {selected_music['music_id']}")
            
            # 记录选择行为
            matcher.log_user_behavior(
                user_id=f"user_{i:03d}",
                action="select_bgm",
                details={"selected_music": selected_music}
            )
        else:
            print("未找到匹配的背景音乐")
        
        time.sleep(1)  # 模拟处理时间
    
    # 3. 展示优化指标
    print("\n" + "=" * 50)
    print("功能优化效果指标")
    print("=" * 50)
    
    metrics = matcher.get_optimization_metrics()
    for key, value in metrics.items():
        print(f"{key}: {value}")
    
    print("\n项目目标达成:")
    print(f"✓ 用户停留时长提升: {metrics['improvement_rate']}")
    print(f"✓ 收集用户反馈: {metrics['feedback_collected']}+ 条")
    print(f"✓ 完成BGM匹配: {metrics['bgm_selection_count']} 次")

if __name__ == "__main__":
    main()