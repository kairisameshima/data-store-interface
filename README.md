# data-store-interface
This is an example build of how one could build a local data store in Python.

A dictionary provides us with the ability to store data in key-value pairs.

To handle transaction behavior, we instantiate a uncommitted copy of the data when beginning a transactions.
All subsequent sets, deletes, and gets are based off of the uncommitted copy until either the transaction is committed or rolled back.