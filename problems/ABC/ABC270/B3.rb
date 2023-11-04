x, y, z = gets.chomp.split.map(&:to_i)
if x * y < 0 
    p x.abs
else
    if z.abs > y.abs
        p -1
    else
        p z.abs + (y - z).abs + (y - x).abs
    end
end