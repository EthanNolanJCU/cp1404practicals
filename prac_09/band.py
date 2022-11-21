class Band():
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def __str__(self):
        return f"{self.name} ({' '.join(str(member) for member in self.members)})"

    def play(self):
        members_instraments = []
        for member in self.members:
            if len(member.instruments) != 0:
                members_instraments.append(f"{member.name} is playing: {member.instruments[0]}")
            else:
                members_instraments.append(f"{member.name} needs an instrament!")
        return "\n".join(members_instraments)

    def add(self, band_member):
        """Add a band member to the band."""
        self.members.append(band_member)