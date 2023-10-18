import os

# from dotenv import load_dotenv
from langchain.llms import OpenAI

##newer one
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import HumanMessagePromptTemplate, ChatPromptTemplate

# load_dotenv()
Description = [
#-----------------------------------------------------------------------------------------------------------------------------------------------------
    """

1 Sienna Crescent for Sale
Welcome to 1 Sienna Crescent, where timeless elegance and spacious living converge to offer an enchanting experience. Upon arrival, you'll be captivated by the home's charm and sophistication. Inside, the design seamlessly connects rooms, creating an open and inviting atmosphere. Every corner of this residence exudes character and style, with meticulous attention to detail. The blend of classic elements and modern finishes crafts a truly unique and welcoming space, perfect for gatherings or cheri moments with loved ones.

The heart of this home is the central living room, providing access to a second living area, an outdoor entertainment space, and a magnificent kitchen with a butler's pantry. The kitchen boasts gas top burners and ample bench space and cupboards for your convenience. This property offers three spacious bedrooms with ceiling fans and built-in wardrobes, while the oversized master bedroom features an ensuite and walk-in robe.

A standout feature of this property is its generous size, situated on an expansive 421m2 block. The spacious outdoor area features a heated pool for year-round enjoyment, creating a haven for relaxation and family fun. The east-facing outdoor entertainment area overlooking undeveloped land adds an extra layer of allure to this family home, providing panoramic views and a sense of spaciousness and privacy.

With ample outdoor space, the possibilities for landscaping and outdoor activities are limitless. Whether you dream of a lush garden, a play area for children, or a serene retreat for relaxation, this property offers a blank canvas for your vision to become a reality.

Additionally, the north-east facing outdoor entertainment area overlooking undeveloped land enhances the sense of spaciousness and tranquility. It's an exceptional feature that can be tailored to your lifestyle, offering endless opportunities for relaxation and enjoyment.

This family home offers a golden opportunity to enjoy timeless elegance and spacious living. From the seamless interior flow to the abundant outdoor space with a heated pool, it seamlessly combines comfort and sophistication. Embrace its captivating charm and create a haven where you can live, relax, and build cheri memories for years to come.

With the completion of the Bruce Highway to Palmview connections expected by the end of this year, access to and from the property will be greatly improved, enhancing overall convenience and connecting you to nearby amenities, schools, shopping centers, and other destinations.

Features include:
- 421m2 block
- Expansive living / dining flowing out to outdoor alfresco
- Large modern kitchen with gas cooking, walk-in butler pantry & dishwasher
- Separate media/multi-purpose room
- Large main bedroom suite with WIR, complete with private ensuite
- 3 additional, equally appointment bedrooms with BIR & ceiling fan
- Generous heated inground pool
- Double lock up garage
- Ducted air conditioning with zoning throughout
- 12 x solar panels
- Picturesque views
- Family friendly neighbourhood
- Close to walking and biking tracks
- Shopping centers, schools, parks, and recreational facilities in close proximity.

""",
#-----------------------------------------------------------------------------------------------------------------------------------------------------

    """
2 Rio Court for Sale
Located on the outskirts of the Jacaranda estate, in a quiet cul-de-sac, is 2 Rio Court. A lowset family home boasting four bedrooms, two bathrooms and multiple living areas.

At the heart of the home is a gourmet kitchen featuring ample cupboard space and electric cooktop. Low maintenance flooring, neutral colour palette, ducted air-conditioning and an outdoor alfresco area make for the perfect abode for the executive couple and families.

Marketing agent Nathan Strudwick says, "Locations don't get more perfect with all amenities practically at your doorstep. This much-loved home is ready and waiting for its new forever family."

Inside:
-Four bedrooms with built-ins
-Master with ensuite & WIR
-Two modern bathrooms
-Gourmet kitchen with electric cooktop
-Open plan living/dining
-Multiple living areas
-Freshly painted
-New carpets
-Ducted air conditioning
-Security screens
-Vertical blinds
-Double garage with internal access

Outside:
-595m2 block
-Outdoor alfresco area
-Fully fenced backyard

Services:
-Town water & sewerage
-NBN ready
-Security alarm - back to base

Location:
-Within the Jacaranda Estate
-2 Minutes to Underwood Marketplace
-3 Minutes to Bunnings
-7 Minutes to Ikea
-Easy access to major arterials
-25 minutes to Brisbane CBD
-40 minutes to the Gold Coast

Disclaimer: We have in preparing this information used our best endeavours to ensure that the information contained herein is true and accurate, but accept no responsibility and disclaim all liability in respect of any errors, omissions, inaccuracies or misstatements that may occur. Prospective purchasers should make their own enquiries to verify the information contained herein.

""",
#-----------------------------------------------------------------------------------------------------------------------------------------------------

    """

If this property is not sold by 5:00pm on the 23rd October 2023, it will be going to Auction at :00pm on the 24th October 2023 at the Harcourts Unite office at /25 Discovery Drive, North Lakes and will also be live streamed with phone bidding allowed.
The owners will consider all offers prior to Auction, so get your offers in before time runs out!

Be quick to inspect this lowset duplex. Beautifully designed is this spacious, modern home with plenty of yard for the kids to play! The meticulous level of thought that went into its design exudes from every surface.

Property Features Include:
- Master suite features A/C, ceiling fan, built-in robe & spacious ensuite
- 2 additional bedrooms with A/C, ceiling fans & built-in robes
- Tiled living/dining with ceiling fan & air conditioning
- Kitchen includes gas cooking, dishwasher & plenty of cupboard space
- Single garage with internal access
- Hall cupboard
- Security screens
- Covered entertaining all overlooking the large fully fenced yard
- 
- Pool and covered BBQ area
- Nestled in a quiet, friendly and desirable location

Located only 10 minutes from Petrie Train Station, 30 minutes from Brisbane CBD and 20 minutes to the airport, this property will suit commuters perfectly. Call Elle today for an inspection before it's too late.

Disclaimer: All photographs, facades, colour schemes, floor plans and dimensions are for illustrative purposes only and may vary slightly to the end product.
This property is being sold by auction or without a price and therefore a price guide cannot be provided. The website may have filtered the property into a price bracket for website functionality purposes.

""",
#-----------------------------------------------------------------------------------------------------------------------------------------------------

    """

Offered to the market for the first time in 5 years and residing in one of Ascot's most sought-after streets, this beloved home presents a remarkable opportunity for families opposite Ascot State School.

Showcasing a character-filled design on a picturesque 830sqm block, the house boasts a perfect northern rear aspect, inviting sensational cross-breezes and sunshine, keeping the entire house bright, open and airy.

The spacious layout has six bedroms, two bathrooms, extensive storage and secure parking. Hosting two living areas and two relaxing poolside retreats, families can gather in the upstairs lounge, dining space, kitchen and entertainer's deck or unwind in the downstairs rumpus and patio, nestled amongst the glistening pool and gorgeous greenery.
o
Exuding timeless appeal, the classic facade, picket fence, and casement windows reflect the charm of yesteryear. Following an extension in the 1970s by leading architect Robin Gibson, the home's original soaring ceilings were lowered but still remain and can be unearthed to further the sense of openness, airiness and character across the property.

Property highlights:
- Charming family home on 830sqm with a perfect northern rear aspect
- Coveted lifestyle position opposite Ascot State School
- Spacious lounge room extending to the dining area and deck
- Galley-style kitchen featuring Asko appliances and a Smeg gas cooktop
- Downstairs rumpus room and undercroft area for kids to ride scooters
- Peaceful entertaining on the upstairs deck and undercover patio
- Saltwater swimming pool, leafy gardens and grassy lawns
- Four bedrooms upstairs, including a master with a retreat and window seat
- Additional two bedroom downstairs
- Two bathrooms (one on each level) and a large seperate laundry downstairs
- Remote driveway gate, remote tandem garage and boat/trailer parking
- Extensive bedroom storage, under-house storage area and workshop
- 3kW solar, Rheem solar hot water system and water softener
- Water tanks servicing the gardens and swimming pool

Offering an unbeatable lifestyle directly opposite Ascot State School, families will love the location and endless convenience. With no traffic or commutes to school in the morning and afternoons, you have more time to spend at Oriel Park, playgrounds and local cafes.
Just 750m from the Oriel Markets and 1.2km from the dining and shopping along Racecourse Road, everything is at your fingertips.
Only steps from bus stops, moments from St Rita's and St Margaret's, and an easy commute to the airport and CBD - this is an incredible opportunity within an esteemed and highly coveted blue-chip suburb.

DISCLAIMER: Whilst all care has been taken to ensure that the information provided herein is correct, we do not take responsibility for any inaccuracies. Accordingly, we recommend that all interested parties should make their own enquiries and due diligence to verify the information.
""",
#-----------------------------------------------------------------------------------------------------------------------------------------------------

    """

Well maintained and recently renovated, this ultra convenient apartment offers 2 large bedrooms and 2 bathrooms including a master bedroom with a walk-in wardrobe and ensuite. Enjoy a waterside lifestyle, bright open plan living in an advantageous location.

- Large master bedroom with ample wardrobe space and ensuite
- Spacious and modern kitchen with ample benchtop and storage space
- Quality combined bathroom and laundry
- Living and dining area leading to the balcony with garden and water views
- 2 undercover balconies from the living room and master bedroom
- Secure basement parking space and storage 
- Waterfront saltwater pool with spa and outdoor seating area
- Onsite management
- Ideal investment


With its walking distance to restaurants, cafes, beaches, parks and playgrounds this perfectly situated apartment has all the perks.

This value packed modern apartment won't last long, contact Mason Niari on 0415755137 to arrange a viewing.

""",
#-----------------------------------------------------------------------------------------------------------------------------------------------------

    """
Presenting a stunning 3-bedroom townhouse in the heart of Caloundra West, meticulously cared for and recently refre with new interior and exterior paint. Every detail has been attended to, ensuring this home is in pristine condition and ready for you to move in and make it your own.

The living area is light and bright with high ceilings and open plan the kitchen is central to the dining space, and lounge area. The entire ground floor is tiled making it perfect for our Sunshine Coast weather, with split system air conditioning for those extra hot days. Step through the glass sliding door to the covered deck, a perfect spot for your morning coffee or cultivating your private herb garden. The lockup garage has plenty of space for your sporty gear as well you car. Not that you will need it.

Upstairs to a master bedroom featuring air conditioning, a walk-in robe, and en-suite. Bedrooms 2 and 3 are also light filled and come complete with ceiling fans and built-in robes. . A study area on the landing and a generous family bathroom with a tub complete the upstairs level.

Enjoy peace of mind in this well-maintained complex. You'll love the welcoming atmosphere of this pet-friendly complex, featuring a fully maintained swimming pool, an garden gazebo and lush tropical gardens and all for a low body corporate fee of $0 per week. Bid farewell to lawn maintenance - it's all taken care of for you!

This prime location allows you to walk to shops, schools, transport options, and nearby parks, making daily life effortlessly convenient. Plus, in just a short 5-minute drive, you'll have access to the stunning Caloundra beaches and all the cafes and restaurants on their shores.

In summary, this property offers excellent value, low-maintenance living, and an unbeatable location. Don't miss out on this incredible opportunity - it's a budget-friendly find that's sure to be in high demand.

Call The Tavis Callard Team to inspect today - 0477990192

""",
#-----------------------------------------------------------------------------------------------------------------------------------------------------

    """

Introducing this spacious one-bedroom apartment located in the highly sought-after suburb of Woolloongabba. Nestled within the boutique Mondrian complex, this property presents a fantastic opportunity for first-time buyers or astute investors seeking a prime Inner City residence.

The apartment features a spacious bedroom with built-in robe, study desk and ensuite access. The modern kitchen features an island bench with stainless steel appliances and electric stove cooktop. Step into this open-plan living area that flows onto the balcony with maximum security. This apartment epitomizes the perfect combination of elegance and practicality, ensuring a lifestyle that exceeds expectations.

Features Include:
- Expansive bedroom with built in robe, ensuite, study nook, balcony access and filled with natural light
- Ensuite is a sleek and stylish oasis, featuring modern fixtures, a spacious shower, and elegant finishes
- Modern kitchen with island stainless steel appliances, cooktop, double sink, an abundance of storage and breakfast bar
- Open plan living and dining with air conditioning
- Tiled kitchen with carpeted living and bedrooms spaces
- Sliding door access onto the balcony ideal for entertaining
- Ample storage throughout
- Ceiling fans throughout
- Lift in building
- Single car space in the secure parking
- Secure building with intercom and security CCTV
- Small boutique community of only 27 apartments

Location Highlights:
- A short stroll to The Gabba Stadium.
- Convenient access to Coles, Australia Post, and specialty shops.
- Bus stop across the road.
- Located down the road from South City Square.
- Near PA, Mater Private, and Queensland Children's Hospitals.
- Less than ten minutes from Southbank Parklands.

Experience the best of convenience and comfort in Woolloongabba, just 1km from the CBD. This lively suburb is packed with delightful cafes and restaurants to explore. With easy access to major transport avenues, including the Pacific Motorway, Airport Link Tunnel, Clem Jones Tunnel, and various train and bus stations, this property is in an ideal location.

Get in contact today for more information or an exclusive viewing!
Show less

""",
#-----------------------------------------------------------------------------------------------------------------------------------------------------

    """

To enquire, please email or call 1300 815 051 and enter code 7389

A beautifully presented, immaculate 4 bedroom family home situated in Residential Parkland at Prestigious Dundowran Beach, set on just under an acre corner block is now for sale. This home presents in top condition and has a stylish, fresh, modern, coastal look.

Just a short stroll to the quiet sandy Dundowran Beach this family haven boasts 4 large double bedrooms, a big living area, separate lounge/media room, two bathrooms and a sparkling in-ground pool plus an extra large 4 bay garage/ (approx. 13.5 x  metres).

The master is a spacious air conditioned room with walk-in robe and ensuite that has a walk-in shower and floating vanity with stone bench top. The other three bedrooms are located at the other end of the home away from the master. The second bedroom has reverse cycle air conditioning, a large robe and is currently used as a study taking in the fantastic views of the landscaped private rear garden. Two further double bedrooms with large robes are spacious and bright. The modern main bathroom has a free standing bath, floating vanity with stone bench top and a walk in shower. There is also a separate toilet. The house also has ceiling fans throughout.

The home has a very spacious kitchen with waterfall bench tops and lots of storage space, fan assisted oven and ceramic cooktop as well as a dishwasher.

The large living area comes with quality features and has a spilt system reverse cycle air conditioner that is large enough to cool or heat the whole living area and additional lounge.

A large patio sliding door opens out to the clay paver covered entertaining area which also spreads down the side of the house with two large seating areas. This is just perfect for all weather entertaining with friends or family whilst overlooking the low maintenance fully fenced very private garden where you can play football, hit a golf ball, swim in the stunning gorgeous in-ground pool or sun bathe under the pergola. There is also a large landscaped dam at the bottom of the garden that can be used for irrigation if required.

As this home sits on a two street access corner block the entertaining area has been carefully planned for privacy and views of the wonderful rear garden. Back inside walk through the barn door into a well appointed separate lounge/media room for those cozy evenings.

The front of the house boasts stylish plantation shutters.

Don't worry about the bills because the 7.kw solar system helps keep them down and as mentioned don't forget that extra large 4 bay garage/ with two remote doors to park the cars and toys. (approx. 13.5 x  metres).

Walk to the Arkarra Tea Gardens for a morning coffee under the Balinese huts and watch the wildlife. There is a local supermarket, chemist and doctor only a short 3-4 minute drive and just a 10-12 minute drive to the CBD, schools, major shops, restaurants and cafes.

About Dundowran Beach. A stunning location with Beachfront acreage living, regarded as one of Fraser Coast's most prestigious residential beach-side suburbs, the region is ideal for home buyers seeking larger allotments within immediate vicinity of the beach.

Book your private viewing as this could be your next home.

To enquire, please email or call 1300 815 051 and enter code 7389

""",
#-----------------------------------------------------------------------------------------------------------------------------------------------------
    """


Perched upon one of Jindalee's most elevated positions more than 25 meters above sea level and in a convenient location, this family home is situated on a 73m2 block, and will appeal to everyone looking for their forever home. With spanning views to the North and cooling breezes all year round, the easy flowing floor plan encompasses indoor and outdoor living areas that fit together to ideally utilize every inch of space.

Upstairs the spacious main living/dining areas takes pride of place and flow perfectly out to the rear balcony overlooking the pool and enjoying views to Mt Coot Tha, making this the perfect spot to enjoy your morning coffee or conclude your day.

There are 4 well-proportioned bedrooms with built-in mirrored robes and brand new carpet on this level. The Master bedroom is positioned away from the other rooms and enjoys air-conditioning, walk through robes and a private ensuite. The large main bathroom services the other rooms and includes a separate shower, bath and toilet.

The spacious kitchen boasts plenty of bench space with a breakfast bar, quality appliances and plenty of storage. Easily serving the living/dining space and poolside alfresco area, this kitchen is perfect for preparing meals for family and guests.

The lower level creates a real sense of space with a separate living area, air-conditioning, toilet, home office, laundry area, direct access to the garage and an oversized workshop! This area offers the perfect privacy for teenagers, the extended family or home business and could be easily transformed to fit your requirements.

- 4 Bedrooms
- Master with Ensuite, walkthrough robes and airconditioning
- 2.5 Bathrooms
- Freshly painted throughout
- Newly poli floors
- Cardiffair, for rapid air extraction
- Lower level with multiple options
- Separate living & dining rooms
- Spacious family kitchen with walk in pantry and quality appliances
- Spacious ground floor living area with separate access and internal stairs
- Covered entertaining area and flat rear yard
- Sparkling pool with sitting area
- Double lock up garage with storage and separate workshop
- Carport for 3rd car accomodation
- Secure 73sqm lot

Located on an elevated 73sqm block, this home is walking distance to all amenities including Jindalee Primary School, Centenary High School, Jindalee Homemaker Centre, DFO, Jindalee boat ramp and conveniently close to City bus stops. Contact Steven Kremer for viewing times and any extra information.

Disclaimer: This property is being sold without a price therefore a price guide cannot be provided. The website may have filtered the property into a price bracket for website functionality purposes.

""",
#-----------------------------------------------------------------------------------------------------------------------------------------------------

    """

Offering a north facing private courtyard and positioned at the end of a boutique complex this generously sized townhome offers the ultimate lifestyle. Featuring refre interiors with great indoor/outdoor flow between the living and dining areas, leading directly to the entertaining area and generous courtyard. This location is unbeatable for those seeking a lifestyle with direct access to Kedron Brook parklands and bikeways.

- Light filled open plan living opens to courtyard
- Entertainers' terrace and easycare lawn
- Refre kitchen with gas cooking, stone benches
- Good sized bedrooms appointed with built-in robes
- Bathroom offers bath, shower recess, separate toilet
- Large master adjoins ensuite and breezy balcony
- Air conditioning, ceiling fans, security screens
- Fenced low maintenance private courtyard
- Powder room, internal access to automated garage
- Only one adjoining wall with your neighbour
- Boutique complex, metres to Kedron Brook Bikeway
- Body Corporate Rates $7.8 per quarter

Lutwyche is six kilometres from the CBD and walking distance to Kedron Brook's spectacular parklands with Prentice Park and Lutwyche Market Central just a short stroll away. Conveniently located only minutes from Lutwyche bus station, linking you with the Northern Busway making it easy travel into the city. Cafes, restaurants, fitness centres, dog off lead area, and schools such as Wooloowin State and Kedron State High are all nearby and only a short drive to the Airport Link and Clem Jones tunnels connecting you to both coasts.""",
]

tags = """
- Alarm System
- dishwasher
- Fireplace
- Gym
- Balcony
- Courtyard
- Pool (Above Ground)
- Pool (Inground)
- Bathroom
- Bedroom
- Kitchen
- Tennis Court
- Broadband
- Built in Robes
- ensuite
- Floor Boards
- Heating Other
- Hot Water Gas
- Hot Water Electric
- Hot Water Solar
- Intercom
- Pay TV
- Rumpus Room
- Spa
- Study
- Vacuum System
- Workshop
- Deck
- Fully Fenced
- Outdoor Entertainment
- Remote Garage
- Secure Parking
- Shed
- Air Conditioning
- Ducted Cooling
- Ducted Heating
- Evaporative Cooling
- Heating Gas
- Heating Electric
- Heating Hydronic
- Reverse Cycle Air Con
- Split System (Heating)
- Split System (Air Con)
- Panels
- Water Tank
"""

template = """

Description = {Description}
tags = {tags}
read the provided Description given above, observe the list of tags present in tags, 
in the answer provide only those tags which are present in both Description and tags.

bundle thsoe tags in list and return it. answer ashould be in list.

"""

key1 = os.environ.get("OPENAI_API_KEY")

def main():
    llm = ChatOpenAI(openai_api_key=key1, temperature=0.0)
    promt_template = ChatPromptTemplate.from_template(template=template)

    for i,each_desc in enumerate(Description,start=1):
        message = promt_template.format_messages(Description=each_desc, tags=tags)
        response = llm(message)
        print(f"tags from description{i}")
        print(response.content)

if __name__ == "__main__":
    main()

# for count, desc in enumerate(descriptions):
#         start = time.time()
#         prompt_template = ChatPromptTemplate.from_template(template_1)
#         message = prompt_template.format_messages(description = desc, tags = tags)

#         res = gpt(message)
#         pred_tags = eval(res.content)
