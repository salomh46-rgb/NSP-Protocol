"""
CLI Tool for Inspecting and Decoding NSP Stream in Real-Time
Usage:
  nsp-inspect decode "⟪#1|0x01|@root|π:Task:ProcessPayment|Σ:99a22861⟫" --lang uz
"""

import argparse
import sys
import io
from nsp_protocol.packet import NSPPacket
from nsp_protocol.decoder import NSPDecoder

if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description="NSP (Neural Semantic Protocol) Frame Inspector")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    decode_parser = subparsers.add_parser("decode", help="Decode an NSP raw frame to human readable text")
    decode_parser.add_argument("frame", type=str, help="Raw NSP frame string e.g. ⟪#1|0x01|...⟫")
    decode_parser.add_argument("--lang", type=str, default="uz", choices=["uz", "en", "ru", "es", "zh", "ar"], help="Owner language")

    args = parser.parse_args()

    if args.command == "decode":
        try:
            packet = NSPPacket.deserialize(args.frame)
            print(NSPDecoder.decode_to_human(packet, lang=args.lang))
        except Exception as e:
            print(f"Error parsing frame: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
