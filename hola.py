def expanded_form(num):
    # creating variables
    expanded = ""
    individual = ""
    holder = 0

    # convert to String
    # split into array
    num = num.to_s.split("")
    zeros = (num.length - 1)

    # Concatenate new string
    num.length.times()
    do | x |:

    # Converting to Integer current character
    holder = num[x].to_i

    # This will add the zeros need
    zeros.times
    do
    holder *= 10


end
zeros -= 1

# If true will skip the rest of this cycle
next if holder == 0

# Convert back to string
holder = holder.to_s

# Concatenating
expanded << holder + " + "
end

# Cutting last characters and returning final string
p
expanded.chomp!(" + ")
end

expanded_form(703)