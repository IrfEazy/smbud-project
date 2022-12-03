import json

import numpy as np


# requires that the type of publication is already assigned to each paper
# add the field location to all paper whose publication_type is Conference
def location_adder(in_file, out_file):
    with open(in_file) as f:
        data = json.load(f)

    locations = ["London, UK",
                 "New York, USA",
                 "Tokyo, Japan",
                 "Paris, France",
                 "Singapore, Singapore",
                 "Amsterdam, Netherlands",
                 "Berlin, Germany",
                 "Seoul, South Korea",
                 "Hong Kong, Hong Kong",
                 "Shanghai, China",
                 "Sydney, Australia",
                 "Los Angeles, USA",
                 "Madrid, Spain",
                 "Melbourne, Australia",
                 "Beijing, China",
                 "Vienna, Austria",
                 "Dubai, UAE",
                 "Toronto, Canada",
                 "Copenhagen, Denmark",
                 "Zurich, Switzerland",
                 "Barcelona, Spain",
                 "Stockholm, Sweden",
                 "Frankfurt, Germany",
                 "San Francisco, USA",
                 "Chicago, USA",
                 "Vancouver, Canada",
                 "Boston, USA",
                 "Brussels, Belgium",
                 "Geneva, Switzerland",
                 "Moscow, Russia",
                 "Dublin, Ireland",
                 "Helsinki, Finland",
                 "Osaka, Japan",
                 "Istanbul, Turkey",
                 "Bangkok, Thailand",
                 "Washington DC, USA",
                 "Taipei, Taiwan",
                 "Kuala Lumpur, Malaysia",
                 "Milan, Italy",
                 "Buenos Aires, Argentina",
                 "Tel Aviv, Israel",
                 "Sao Paulo, Brazil",
                 "Fukuoka, Japan",
                 "Mexico City, Mexico",
                 "Jakarta, Indonesia",
                 "Cairo, Egypt",
                 "Johannesburg, South Africa",
                 "Mumbai, India"]

    for i in range(len(data)):
        if data[i]["publication_type"] == "Conference":
            data[i]["location"] = locations[np.random.randint(0, len(locations))]

    with open(out_file, 'w') as f:
        json.dump(data, f, indent=4)
