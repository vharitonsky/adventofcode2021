const std = @import("std");
const io = std.io;
const ArrayList = std.ArrayList;
const test_allocator = std.testing.allocator;

fn part1(measurements: []u16) u16 {
    var incs: u16 = 0;
    for (measurements[1..measurements.len]) |m, index|{
        if(m > measurements[index]) {
            incs += 1;
        }
    }
    return incs;
}

fn part2(measurements: []u16) !u16 {
    var windowList = ArrayList(u16).init(test_allocator);
    for (measurements[0..measurements.len - 3]) |m, index|{
        try windowList.append(measurements[index] + measurements[index + 1] + measurements[index + 2]);
    }
    var windows: []u16 = windowList.allocatedSlice();
    var incs: u16 = 0;
    for (windows[1..windows.len]) |w, index|{
        if(w > windows[index]) {
            incs += 1;
        }
    }
    return incs;
}

pub fn main() anyerror!void {
    var measurements = [_]u16{199, 200, 208, 210, 200, 207, 240, 269, 260, 263};
    var slice: []u16 = &measurements;
    var answer:u16 = part1(slice);
    var answer2: anyerror!u16 = part2(slice);
    std.log.info("{d}", .{answer});
    std.log.info("{d}", .{answer2});

    var file = try std.fs.cwd().openFile("task1_input", .{});
    defer file.close();
    var buf_reader = io.bufferedReader(file.reader());
    var in_stream = buf_reader.reader();
    var buf: [1024]u8 = undefined;
    var measurementsList = ArrayList(u16).init(test_allocator);
    while (try in_stream.readUntilDelimiterOrEof(&buf, '\n')) |line| {
        var number: u16 = try std.fmt.parseInt(u16, line, 10);
        try measurementsList.append(number);
    }
    answer = part1(measurementsList.allocatedSlice());
    answer2 = part2(measurementsList.allocatedSlice());
    std.log.info("{d}", .{answer});
    std.log.info("{d}", .{answer2});
}
