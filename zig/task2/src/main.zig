const std = @import("std");
const io = std.io;
const ascii = std.ascii;
const ArrayList = std.ArrayList;
const test_allocator = std.testing.allocator;

//def part_1(instructions):
//    horizontal = 0
//    vertical = 0
//    for instr in instructions:
//        if instr.startswith("forward "):
//            horizontal += int(instr.split()[1])
//        elif instr.startswith("down "):
//            vertical += int(instr.split()[1])
//        else:
//            vertical -= int(instr.split()[1])
//    return horizontal * vertical


fn part_1(instructions: ArrayList([]u8)) anyerror!u16{
    var horizontal: u16 = 0;
    var vertical: u16 = 0;
    for (instructions.allocatedSlice()) |instr, index| {
        if(ascii.startsWithIgnoreCase(instr, "forward ")) {
            const startSpace = ascii.indexOfIgnoreCase(instr, " ");
            if (startSpace) |start| {
                var number =  try std.fmt.parseInt(u16, instr[start + 1..instr.len], 10);
                horizontal += number;
            }
        }
        else if(ascii.startsWithIgnoreCase(instr, "down ")) {
            const startSpace = ascii.indexOfIgnoreCase(instr, " ");
            if (startSpace) |start| {
                var number =  try std.fmt.parseInt(u16, instr[start + 1..instr.len], 10);
                vertical += number;
            }
        }
        else if(ascii.startsWithIgnoreCase(instr, "up ")) {
            const startSpace = ascii.indexOfIgnoreCase(instr, " ");
            if (startSpace) |start| {
                var number =  try std.fmt.parseInt(u16, instr[start + 1..instr.len], 10);
                vertical -= number;
            }
        }
    }
    return horizontal * vertical;
}

pub fn main() anyerror!void {
    var instructions = ArrayList([]u8).init(test_allocator);
    var file = try std.fs.cwd().openFile("task2_input", .{});
    defer file.close();
    var buf_reader = io.bufferedReader(file.reader());
    var in_stream = buf_reader.reader();
    var buf: [1024]u8 = undefined;
    while (try in_stream.readUntilDelimiterOrEof(&buf, '\n')) |line| {
        try instructions.append(buf[0..10]);
    }
//      [_]u8{"down 5"},
//      [_]u8{"forward"},
//      [_]u8{"up 3"},
//      [_]u8{"down 8"},
//      [_]u8{"forward 2"}
//    };
    std.log.info("part_1: {d}", .{part_1(instructions)});
}
