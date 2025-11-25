"""Test script for topic rotation logic"""
import sys
import json
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from channel_poster import get_topic_for_time, load_state, save_state, STATE_FILE

def test_rotation():
    """Test the topic rotation logic"""
    print("=" * 60)
    print("TESTING TOPIC ROTATION LOGIC")
    print("=" * 60)
    
    # Reset state
    STATE_FILE.unlink(missing_ok=True)
    print("\n✓ State file reset")
    
    # Test schedule
    test_schedule = [
        (9, "energy", "✨ Energy of the Day"),
        (14, "space", "🌌 Space (first time)"),
        (14, "science", "🔬 Science (second time)"),
        (14, "space", "🌌 Space (third time - rotation)"),
        (19, "technology", "🤖 Technology (first time)"),
        (19, "nature", "🌿 Nature (second time)"),
        (19, "technology", "🤖 Technology (third time - rotation)"),
        (22, "space", "🌌 Space (night mysticism)"),
    ]
    
    print("\n" + "=" * 60)
    print("Testing rotation sequence:")
    print("=" * 60)
    
    for hour, expected_topic, description in test_schedule:
        actual_topic = get_topic_for_time(hour)
        status = "✅" if actual_topic == expected_topic else "❌"
        print(f"{status} {hour:02d}:00 → {actual_topic:12} (expected: {expected_topic:12}) - {description}")
    
    # Show final state
    final_state = load_state()
    print("\n" + "=" * 60)
    print("Final rotation state:")
    print("=" * 60)
    print(f"  14:00 rotation index: {final_state['day_rotation_index']}")
    print(f"  19:00 rotation index: {final_state['evening_rotation_index']}")
    
    print("\n" + "=" * 60)
    print("Next posts will be:")
    print("=" * 60)
    print(f"  09:00 → energy (fixed)")
    print(f"  14:00 → {'space' if final_state['day_rotation_index'] == 0 else 'science'}")
    print(f"  19:00 → {'technology' if final_state['evening_rotation_index'] == 0 else 'nature'}")
    print(f"  22:30 → space (fixed)")
    
    print("\n" + "=" * 60)
    print("TEST COMPLETE!")
    print("=" * 60)

if __name__ == "__main__":
    test_rotation()
