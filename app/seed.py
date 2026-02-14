# seed.py - Corrected Version
from genre.models import Collection, Piece  # Replace 'myapp' with your actual app name

# First, let's clear existing data (optional - comment this out if you want to keep existing data)
print("Clearing existing data...")
Piece.objects.all().delete()
Collection.objects.all().delete()
print("Existing data cleared.")

# Create Collections
collections_data = [
    {
        'name': 'Classical Masterpieces',
        'description': 'Timeless classical compositions from the greatest composers',
        'cover': 'https://images.unsplash.com/photo-1507838153414-b4b713384a76?w=500'
    },
    {
        'name': 'Jazz Standards',
        'description': 'Essential jazz pieces that defined the genre',
        'cover': 'https://images.unsplash.com/photo-1511192338575-1126ce2971f9?w=500'
    },
    {
        'name': 'Rock Classics',
        'description': 'Legendary rock anthems from the 60s to today',
        'cover': 'https://images.unsplash.com/photo-1498038432885-c6f3f1b912ee?w=500'
    },
    {
        'name': 'Electronic Vibes',
        'description': 'Modern electronic and ambient masterpieces',
        'cover': 'https://images.unsplash.com/photo-1571266028243-3716f02d2d2f?w=500'
    },
    {
        'name': 'World Music',
        'description': 'Traditional and contemporary music from around the globe',
        'cover': 'https://images.unsplash.com/photo-1514320291840-2e0a9bf2a9ae?w=500'
    }
]

# Create collections and store them in a dictionary for reference
collections = {}
for coll_data in collections_data:
    collection, created = Collection.objects.get_or_create(
        collection_name=coll_data['name'],
        defaults={
            'description': coll_data['description'],
            'collcover': coll_data['cover']
        }
    )
    collections[coll_data['name']] = collection
    print(f"{'Created' if created else 'Found'} collection: {collection.collection_name}")

# Pieces data organized by collection - FIXED: All entries now have all required fields
pieces_data = {
    'Classical Masterpieces': [
        {'title': 'Symphony No. 5', 'typ': 'Symphony', 'artist': 'Ludwig van Beethoven', 'year': 1808, 'cover': 'https://images.unsplash.com/photo-1589903308904-1010c2294adc?w=500'},
        {'title': 'Clair de Lune', 'typ': 'Piano Suite', 'artist': 'Claude Debussy', 'year': 1905, 'cover': 'https://images.unsplash.com/photo-1520523839897-bd0b52f945a0?w=500'},
        {'title': 'The Four Seasons - Spring', 'typ': 'Violin Concerto', 'artist': 'Antonio Vivaldi', 'year': 1723, 'cover': 'https://images.unsplash.com/photo-1507838153414-b4b713384a76?w=500'},
        {'title': 'Eine kleine Nachtmusik', 'typ': 'Serenade', 'artist': 'Wolfgang Amadeus Mozart', 'year': 1787, 'cover': 'https://images.unsplash.com/photo-1552422535-c45813c61732?w=500'},
        {'title': 'Ride of the Valkyries', 'typ': 'Opera', 'artist': 'Richard Wagner', 'year': 1856, 'cover': 'https://images.unsplash.com/photo-1507838153414-b4b713384a76?w=500'},
    ],
    'Jazz Standards': [
        {'title': 'Take Five', 'typ': 'Cool Jazz', 'artist': 'Dave Brubeck', 'year': 1959, 'cover': 'https://images.unsplash.com/photo-1511192338575-1126ce2971f9?w=500'},
        {'title': 'So What', 'typ': 'Modal Jazz', 'artist': 'Miles Davis', 'year': 1959, 'cover': 'https://images.unsplash.com/photo-1415201364774-f6f0bb35f28f?w=500'},
        {'title': 'My Favorite Things', 'typ': 'Vocal Jazz', 'artist': 'John Coltrane', 'year': 1961, 'cover': 'https://images.unsplash.com/photo-1511192338575-1126ce2971f9?w=500'},
        {'title': 'Round Midnight', 'typ': 'Ballad', 'artist': 'Thelonious Monk', 'year': 1944, 'cover': 'https://images.unsplash.com/photo-1558584673-c834fb1cc3ca?w=500'},
    ],
    'Rock Classics': [
        {'title': 'Bohemian Rhapsody', 'typ': 'Progressive Rock', 'artist': 'Queen', 'year': 1975, 'cover': 'https://images.unsplash.com/photo-1498038432885-c6f3f1b912ee?w=500'},
        {'title': 'Stairway to Heaven', 'typ': 'Hard Rock', 'artist': 'Led Zeppelin', 'year': 1971, 'cover': 'https://images.unsplash.com/photo-1498038432885-c6f3f1b912ee?w=500'},
        {'title': 'Like a Rolling Stone', 'typ': 'Folk Rock', 'artist': 'Bob Dylan', 'year': 1965, 'cover': 'https://images.unsplash.com/photo-1498038432885-c6f3f1b912ee?w=500'},
        {'title': 'Smells Like Teen Spirit', 'typ': 'Grunge', 'artist': 'Nirvana', 'year': 1991, 'cover': 'https://images.unsplash.com/photo-1498038432885-c6f3f1b912ee?w=500'},
        {'title': 'Hotel California', 'typ': 'Rock', 'artist': 'Eagles', 'year': 1976, 'cover': 'https://images.unsplash.com/photo-1498038432885-c6f3f1b912ee?w=500'},
    ],
    'Electronic Vibes': [
        {'title': 'Midnight City', 'typ': 'Synth-pop', 'artist': 'M83', 'year': 2011, 'cover': 'https://images.unsplash.com/photo-1571266028243-3716f02d2d2f?w=500'},
        {'title': 'Strobe', 'typ': 'Progressive House', 'artist': 'deadmau5', 'year': 2009, 'cover': 'https://images.unsplash.com/photo-1571266028243-3716f02d2d2f?w=500'},
        {'title': 'Roygbiv', 'typ': 'IDM', 'artist': 'Boards of Canada', 'year': 1998, 'cover': 'https://images.unsplash.com/photo-1571266028243-3716f02d2d2f?w=500'},
    ],
    'World Music': [
        {'title': 'Baba Yetu', 'typ': 'African', 'artist': 'Christopher Tin', 'year': 2005, 'cover': 'https://images.unsplash.com/photo-1514320291840-2e0a9bf2a9ae?w=500'},
        {'title': 'Chan Chan', 'typ': 'Cuban Son', 'artist': 'Buena Vista Social Club', 'year': 1997, 'cover': 'https://images.unsplash.com/photo-1514320291840-2e0a9bf2a9ae?w=500'},
        {'title': 'Djorolen', 'typ': 'African Pop', 'artist': 'Angelique Kidjo', 'year': 2007, 'cover': 'https://images.unsplash.com/photo-1514320291840-2e0a9bf2a9ae?w=500'},
    ]
}

# Create pieces for each collection
for collection_name, pieces in pieces_data.items():
    collection = collections.get(collection_name)
    if collection:
        for piece_data in pieces:
            # FIXED: Using correct field names
            piece, created = Piece.objects.get_or_create(
                title=piece_data['title'],
                artist=piece_data['artist'],
                defaults={
                    'collection': collection,
                    'typ': piece_data['typ'],
                    'year': piece_data['year'],
                    'piececover': piece_data['cover']  # This maps to 'piececover' field
                }
            )
            print(f"{'Created' if created else 'Found'} piece: {piece.title} in {collection_name}")
    else:
        print(f"Collection {collection_name} not found!")

print("\n" + "="*50)
print("✅ SEEDING COMPLETE!")
print("="*50)
print(f"Total Collections: {Collection.objects.count()}")
print(f"Total Pieces: {Piece.objects.count()}")
print("="*50)

# Optional: Show summary by collection
print("\n📊 Summary by Collection:")
for collection in Collection.objects.all():
    piece_count = Piece.objects.filter(collection=collection).count()
    print(f"  • {collection.collection_name}: {piece_count} pieces")